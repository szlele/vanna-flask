
from dotenv import load_dotenv
import os
from vanna.openai.openai_chat import OpenAI_Chat
from vanna.milvus.milvus_vector import Milvus_VectorStore
from openai import OpenAI
from pymilvus import MilvusClient
from pymilvus.model.dense.openai import OpenAIEmbeddingFunction

load_dotenv()

class Extra_OpenAI_Chat(OpenAI_Chat):
    def __init__(self,config={}):
        super().__init__(config)

    def submit_prompt(self, prompt, **kwargs) -> str:
        if prompt is None:
            raise Exception("Prompt is None")

        if len(prompt) == 0:
            raise Exception("Prompt is empty")

        response = self.client.chat.completions.create(
                model=os.environ["OPENAI_LLM_MODEL"],
                messages=prompt,
                stop=None,
                temperature=self.temperature,
                extra_body={
                    "chat_template_kwargs": {
                        "enable_thinking": False
                    }
                }
            )

        for choice in response.choices:
            if "text" in choice:
                return choice.text

        return response.choices[0].message.content
    
class VannaService(Extra_OpenAI_Chat,Milvus_VectorStore):
    def __init__(self):
        config={}
        config["milvus_client"] = MilvusClient(
                uri = os.environ["MILVUS_URI"],
                user = os.environ["MILVUS_USER"],
                password = os.environ["MILVUS_PASSWORD"])
            
        config["embedding_function"] = OpenAIEmbeddingFunction(
                model_name = os.environ["OPENAI_EMBEDDING_MODEL"],
                api_key = os.environ["OPENAI_EMBEDDING_API_KEY"],
                base_url = os.environ["OPENAI_EMBEDDING_BASE_URL"],
            )
            
        # 配置milvus
        Milvus_VectorStore.__init__(self, config)
        # 配置openai
        OpenAI_Chat.__init__(self,
            client=OpenAI(
                api_key = os.environ["OPENAI_LLM_API_KEY"],
                base_url = os.environ["OPENAI_LLM_BASE_URL"]),
            config=config)
        # 配置mysql连接
        super().connect_to_mysql(
            host = os.environ["MYSQL_HOST"],
            dbname = os.environ["MYSQL_DBNAME"],
            user = os.environ["MYSQL_USER"],
            password = os.environ["MYSQL_PASSWORD"],
            port = int(os.environ["MYSQL_PORT"]))

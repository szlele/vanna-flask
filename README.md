# vanna-flask
全部组件本地部署的vanna-flask

- LLM服务：基于VLLM部署的Qwen3-8B模型服务
- Embedding服务：基于VLLM部署的Qwen3-Embedding-8B模型服务
- 数据库服务：基于MySQL数据库服务
- 向量数据库服务：基于Milvus向量数据库服务

# 安装步骤

## 配置`.env`
```
# LLM模型配置
OPENAI_LLM_MODEL=
OPENAI_LLM_API_KEY=sk-
OPENAI_LLM_BASE_URL=

# Embedding模型配置
OPENAI_EMBEDDING_MODEL=
OPENAI_EMBEDDING_API_KEY=sk-
OPENAI_EMBEDDING_BASE_URL=

# 向量数据库配置
MILVUS_URI=
MILVUS_USER=admin
MILVUS_PASSWORD=123456

# 关系型数据库配置
MYSQL_HOST=
MYSQL_PORT=3306
MYSQL_DBNAME=vanna
MYSQL_USER=root
MYSQL_PASSWORD=123456
```

## 启动服务
```
docker compose up -d
```

## 访问服务
```
http://localhost:8080
```


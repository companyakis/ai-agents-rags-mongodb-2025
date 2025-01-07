from pymilvus import MilvusClient

# let's create a local Milvus vector database

local_db = MilvusClient("milvus_learning.db")

print(local_db) # <pymilvus.milvus_client.milvus_client.MilvusClient object at 0x7aa921e0d0c0>

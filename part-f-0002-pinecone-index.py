"""
Indexes are used to store records, including the vectors and associated metadata, as well as serving queries and other manipulations
"""

# Import ServerlessSpec
from pinecone import ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_41wZVX_CdXJXBgp3ZdfUwFuBx6PLfgFxde8VnCWdRXDDC7MPzykb9oCk54TTNLjTiTA63v")

pc.delete_index('my-first-index')

# Create your Pinecone index
pc.create_index(
    name="my-first-index",
    dimension=256,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)


import os
#responsible for creating embeddings in vector store
from langchain_openai import AzureOpenAIEmbeddings
import openai
from langchain.vectorstores.azuresearch import AzureSearch
from langchain_community.document_loaders import AzureBlobStorageContainerLoader
#container we will use to store our container data 
from langchain.text_splitter import CharacterTextSplitter
#create chunks from txt file

from dotenv import load_dotenv

load_dotenv()
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")


vector_store_address: str = f"https://{os.environ.get('AZURE_COGNITIVE_SEARCH_SERVICE_NAME')}.search.windows.net"


embeddings = AzureOpenAIEmbeddings(
    azure_deployment="embeddingmodel",  # Replace with your actual deployment name
    openai_api_version="2023-05-15",  # Specify the API version you are using
)

index_name: str = "langchain-vector-stonybrook"

vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=os.environ.get("AZURE_COGNITIVE_SEARCH_API_KEY"),
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)


loader = AzureBlobStorageContainerLoader(
    conn_str=os.environ.get("AZURE_CONN_STRING"),
    container=os.environ.get("CONTAINER_NAME"),
)

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)
vector_store.add_documents(documents=docs)
print("Data loaded into vectorstore successfully")

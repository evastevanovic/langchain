import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
# 1. Import OllamaEmbeddings instead of OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv()

if __name__ == '__main__':
    print("Ingesting...")
    
    loader = TextLoader("/home/evastevanovic/personal/langchain-course/mediumblog1.txt")
    document = loader.load()

    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")

    # tutorial
    # embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get("OPENAI_API_KEY"))

    # ollama version

    # 2. Initialize the local Qwen model (No API key required!)
    embeddings = OllamaEmbeddings(
        model="qwen3-embedding:0.6b"
    )



    print("ingesting...")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])

    print("finish")


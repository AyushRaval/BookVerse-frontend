from src.helper import load_pdf_file, text_split, download_huggingface_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone

from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv()
PINECONE_API_KEY= os.environ.get("PINECONE_API_KEY")


extracted_data=load_pdf_file(data='data/')
text_chunks=text_split(extracted_data)
embeddings=download_huggingface_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name="medical-chatbot"

#embed each chunk and upsert the embeddings into your Pinecone index
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)
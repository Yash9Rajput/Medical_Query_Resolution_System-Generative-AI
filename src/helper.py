from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


#loading the data 
def load_pdf_files(data):
    loader = DirectoryLoader(data,
                             glob = "*.pdf",
                             loader_cls= PyPDFLoader)
    
    document = loader.load()
    
    return document



#splitting the data into chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    
    return text_chunks


def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings



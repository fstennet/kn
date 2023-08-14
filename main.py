# Import libraries
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader

def load_documents(path):
    loader = DirectoryLoader(path, glob='**/*.*')
    return loader.load()

def split_text(doc):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(doc)

def setup_db(docs, embedding):
    
    return Chroma.from_documents(documents=docs,
                                     embedding=embedding,
                                     persist_directory=persist_directory)

if __name__ == '__main__':

    persist_directory = 'db'

    embedding = OpenAIEmbeddings()

    documents = load_documents('data/optimus')
    splitted_docs = split_text(documents)

    db = setup_db(splitted_docs, embedding)

    

    


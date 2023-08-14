from langchain.chat_models import ChatOpenAI
import sys
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

def load_db(embedding, dir):
    return Chroma(embedding_function=embedding, persist_directory=dir)

def create_retriever(db):
    return db.as_retriever()

def create_chain(llm, retriever):
    return RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=retriever,
                                  return_source_documents=True,
                                  verbose=True)
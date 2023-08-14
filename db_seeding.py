# Import libraries
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader

def load_documents(path):
    loader = DirectoryLoader(path, glob='**/*.*')
    return loader.load()

def split_text(doc):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(doc)

def setup_db(docs, embedding, dir):
    return Chroma.from_documents(documents=docs,
                                     embedding=embedding,
                                     persist_directory=dir)

if __name__ == '__main__':

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        raise Exception('db or document_path param missing. Usage: db_seeding.py "db folder name" "location of source documents"')

    db_param = sys.argv[1]
    document_path_param = sys.argv[2]

    embedding = OpenAIEmbeddings()

    documents = load_documents(document_path_param)
    splitted_docs = split_text(documents)

    db = setup_db(splitted_docs, embedding, db_param)
    db.persist()

    print('Database created.')

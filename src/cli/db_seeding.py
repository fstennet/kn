import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings, SentenceTransformerEmbeddings
from langchain.document_loaders import DirectoryLoader

def load_documents(path):
    loader = DirectoryLoader(path, glob='**/*.*', recursive=True)
    return loader.load()

def split_text(doc):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200).from_language(language=Language.PHP)
    return text_splitter.split_documents(doc)

def setup_db(docs, embedding, dir):
    return Chroma.from_documents(documents=docs,
                                     embedding=embedding,
                                     persist_directory=dir)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        raise Exception('db or document_path param missing. Usage: db_seeding.py "db name" "document_path"')

    db_param = sys.argv[1]
    document_path_param = sys.argv[2]

    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    documents = load_documents(document_path_param)
    splitted_docs = split_text(documents)

    db = setup_db(splitted_docs, embedding, db_param)
    db.persist()

    print('Database created and seeded.')

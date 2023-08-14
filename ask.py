# Import libraries
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

def parse_response(response):
    print(response['result'])
    print('\nSources:')
    for source in response['source_documents']:
        print(source.metadata['source'])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('db or query param missing. Usage: main.py "db folder name" "query to make"')
    db_param = sys.argv[1]
    query = sys.argv[2]

    embedding = OpenAIEmbeddings()

    db = load_db(embedding, db_param)
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    retriever = create_retriever(db)

    chain = create_chain(llm=llm, retriever=retriever)

    response = chain(query)

    parse_response(response=response)
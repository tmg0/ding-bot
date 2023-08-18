from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from utils.conf import load_config
from utils.openai import embeddings_model, text_splitter

import glob

persist_directory = load_config().chroma_persist_directory


def load_pdf_docs(pattern):
    documents = []
    file_paths = glob.glob(pattern)

    if len(file_paths) == 0:
        return

    for file_paths in file_paths:
        docs = PyPDFLoader(file_paths).load()
        documents = documents + text_splitter.split_documents(documents=docs)

    Chroma.from_documents(documents=documents, embedding=embeddings_model)

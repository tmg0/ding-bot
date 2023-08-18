from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from utils.conf import load_config
from utils.openai import embeddings_model

import glob

persist_directory = load_config().chroma_persist_directory


def load_pdf_docs(pattern):
    documents = []
    file_paths = glob.glob(pattern)

    if len(file_paths) == 0:
        return

    for file_paths in file_paths:
        loader = PyPDFLoader(file_paths)
        d = loader.load_and_split()
        documents = documents + d

    Chroma.from_documents(documents=documents, embedding=embeddings_model)

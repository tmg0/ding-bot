from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.conf import load_config
import os

conf = load_config()
os.environ["OPENAI_PROXY"] = conf.openai_proxy

llm = OpenAI(openai_api_key=conf.openai_api_key)
embeddings_model = OpenAIEmbeddings(openai_api_key=conf.openai_api_key)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)

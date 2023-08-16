from langchain.llms import OpenAI
from utils.conf import load_config
import os

conf = load_config()
os.environ["OPENAI_PROXY"] = conf.openai_proxy

llm = OpenAI(openai_api_key=conf.openai_api_key, temperature=0.9)

from common import fse
from langchain.llms import OpenAI

import os

conf = fse.read_yaml(path="./bot.config.yaml")

os.environ["OPENAI_PROXY"] = conf["openai_proxy"]

llm = OpenAI(openai_api_key=conf["openai_api_key"], temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))

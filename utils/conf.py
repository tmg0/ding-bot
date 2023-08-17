from utils.fs import read_yaml


class BotConfig:
    def __init__(self, json):
        self.openai_api_key = json["openai_api_key"]
        self.openai_proxy = json["openai_proxy"]
        self.chroma_persist_directory = json["chroma_persist_directory"]


def load_config(name="bot"):
    json = read_yaml(name + ".config.yaml")
    return BotConfig(json=json)

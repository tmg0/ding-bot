from pydantic import BaseModel
from langchain.vectorstores import Chroma
from utils.router import router
from utils.conf import load_config
from utils.openai import text_splitter, embeddings_model

persist_directory = load_config().chroma_persist_directory


class EmbeddingsReq(BaseModel):
    input: str


@router.post("/embeddings")
async def embeddings(req: EmbeddingsReq):
    texts = text_splitter.split_text(req.input)
    embedding = embeddings_model
    Chroma.from_texts(texts, embedding, persist_directory).persist()
    return len(texts)

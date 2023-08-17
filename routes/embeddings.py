from pydantic import BaseModel
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from utils.router import router
from utils.llm import text_splitter


class EmbeddingsReq(BaseModel):
    input: str


@router.post("/embeddings")
async def index(req: EmbeddingsReq):
    texts = text_splitter.split_text(req.input)
    embedding = OpenAIEmbeddings()
    Chroma.from_texts(texts, embedding).persist()
    return len(texts)

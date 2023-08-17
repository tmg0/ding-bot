from pydantic import BaseModel
from langchain.vectorstores import Chroma
from utils.router import router
from utils.openai import text_splitter, embeddings_model


class EmbeddingsReq(BaseModel):
    input: str


@router.post("/embeddings")
async def index(req: EmbeddingsReq):
    texts = text_splitter.split_text(req.input)
    embeddings = embeddings_model.embed_documents(texts)
    Chroma.from_texts(texts, embeddings).persist()
    return len(texts)

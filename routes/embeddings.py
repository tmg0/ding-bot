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
    Chroma.from_texts(
        texts, embedding=embeddings_model, persist_directory=persist_directory
    ).persist()
    return texts

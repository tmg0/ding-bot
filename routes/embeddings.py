from pydantic import BaseModel
from utils.router import router
from utils.llm import text_splitter


class EmbeddingsReq(BaseModel):
    input: str


@router.post("/embeddings")
async def index(req: EmbeddingsReq):
    splits = text_splitter.split_text(req.input)
    return len(splits)

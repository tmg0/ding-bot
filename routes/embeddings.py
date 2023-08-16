from pydantic import BaseModel
from utils.router import router


class EmbeddingsReq(BaseModel):
    input: str


@router.post("/embeddings")
async def index(req: EmbeddingsReq):
    return req.input

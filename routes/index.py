from pydantic import BaseModel
from utils.router import router
from utils.llm import llm


class IndexReq(BaseModel):
    content: str


@router.post("/")
async def index(req: IndexReq):
    return llm(req.content)

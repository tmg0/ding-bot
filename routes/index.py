from pydantic import BaseModel
from common.router import router
from common.llm import llm


class IndexReq(BaseModel):
    content: str


@router.post("/")
async def index(req: IndexReq):
    return llm(req.content)

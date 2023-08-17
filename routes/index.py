from pydantic import BaseModel
from langchain.vectorstores import Chroma
from utils.conf import load_config
from utils.router import router
from utils.openai import llm
from utils.openai import embeddings_model
from langchain.chains.question_answering import load_qa_chain

persist_directory = load_config().chroma_persist_directory


class IndexReq(BaseModel):
    content: str


@router.post("/")
async def index(req: IndexReq):
    db3 = Chroma(
        persist_directory=persist_directory, embedding_function=embeddings_model
    )
    docs = db3.similarity_search(req.content)
    chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
    return chain.run(input_documents=docs, question=req.content)

from fastapi import FastAPI
from utils.bootstrap import bootstrap
from utils.loader import load_pdf_docs

app = FastAPI()
bootstrap(app)

if __name__ == "__main__":
    import uvicorn

    load_pdf_docs("./pdf_docs/*.pdf")
    uvicorn.run("main:app", host="localhost", port=5174, reload=True)

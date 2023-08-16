from fastapi import FastAPI
from utils.router import resolve_routes

app = FastAPI()
resolve_routes(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=5174, reload=True)

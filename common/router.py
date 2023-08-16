from fastapi import APIRouter
from common.fs import import_glob

router = APIRouter()


def resolve_routes(app):
    import_glob("routes/*.py")
    app.include_router(router)

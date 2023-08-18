from utils.router import resolve_routes


def bootstrap(app):
    resolve_routes(app)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.routes import router

__version__ = "0.3.3"


def get_application() -> FastAPI:
    app = FastAPI(
        title="ChunkVault - Lite",
        version=__version__,
        root_path="/api",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app

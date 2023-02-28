from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application import __version__
from application.routes import router


def startup() -> FastAPI:
    app_base = FastAPI(
        title="ChunkVault-Lite - Deta Space Backend",
        version=__version__,
        root_path="/api-v1"
    )

    app_base.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app_base.include_router(router)

    return app_base


app = startup()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, root_path="")

from fastapi import FastAPI

from application import __version__
from application.routes import router

def startup() -> FastAPI:
    app = FastAPI(
        tittle="ChunkVault - Deta Backend",
        version=__version__,
    )

    app.include_router(router)

    return app

app = startup()

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
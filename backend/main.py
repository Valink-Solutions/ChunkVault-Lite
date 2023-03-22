import uvicorn
from application import get_application

app = get_application()


def start():
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, root_path="")


if __name__ == "__main__":
    start()

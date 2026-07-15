from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"message": "Ola mundo"}

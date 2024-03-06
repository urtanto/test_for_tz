from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str, message: str):
    return {"message": f"Hello {name}! {message}!"}

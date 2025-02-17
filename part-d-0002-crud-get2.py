from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(area: str = "AI"):
    return {"message": f"Welcome {area}!"}

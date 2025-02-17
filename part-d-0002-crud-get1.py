from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"purpose": "Full-stack AI"}

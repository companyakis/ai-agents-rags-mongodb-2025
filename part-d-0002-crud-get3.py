from fastapi import FastAPI

app = FastAPI()

# index

@app.get("/")
async def index() -> dict[str, str]:
    return {"my_name": "Mustafa Büyükdereli"}

# contact

@app.get("/contact")
async def contact() -> str:
    return "lorem.ipsum@mustafa.com"

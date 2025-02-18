from fastapi import FastAPI

app = FastAPI()

EMPLOYEES = [
    {"id": 100, "name": "Ayhan Bilici", "department": "Sales"},
    {"id": 321, "name": "Bengü Arslan", "department": "Operations"},
    {"id": 438, "name": "Jale Cüce", "department": "Marketing"},
    {"id": 632, "name": "Serhat Aferin", "department": "Accounting"},
]

@app.get("/employees")
async def employees() -> list[dict]:
    return EMPLOYEES
    

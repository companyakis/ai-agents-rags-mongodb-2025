from fastapi import FastAPI, HTTPException

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
    
@app.get("/employees/{emp_id}")
async def employee(emp_id: int) -> dict:
    
    employee = next((emp for emp in EMPLOYEES if emp["id"] == emp_id), None)
    
    if employee is None:
        raise HTTPException(status_code = 404, detail = "Employee not found!")
    
    return employee

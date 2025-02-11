from pydantic import BaseModel

class EmployeeMessage(BaseModel):
    name: str
    id: int
    content: str
    
emp_msg1 = EmployeeMessage(name = "Ayhan Bilir", id = 1245, content = "I'm unhappy. Please, give me more time...")

print(emp_msg1) # name='Ayhan Bilir' id=1245 content="I'm unhappy. Please, give me more time..."

print(emp_msg1.content) # I'm unhappy. Please, give me more time...

emp_msg2 = EmployeeMessage(name = "Bengü Göğebakan", id = "1245", content = "Let's take action...") # Argument of type "Literal['1245']" cannot be assigned to parameter "id" of type "int" in function "__init__"



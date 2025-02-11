from pydantic import BaseModel
from typing import Optional

class EmployeeMessage(BaseModel):
    name: str
    id: int
    content: str
    department: Optional[str] = None
    

emp_msg1 = EmployeeMessage(name="Ayhan Bilir", id= 1245, content="Lorem ipsum", department="HR")

print(emp_msg1)

emp_msg2 = EmployeeMessage(name="Ayhan Bilir", id= 1245, content="ceteris paribus")
    
print(emp_msg2)

# name='Ayhan Bilir' id=1245 content='Lorem ipsum' department='HR'
# name='Ayhan Bilir' id=1245 content='ceteris paribus' department=None

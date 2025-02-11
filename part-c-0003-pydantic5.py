from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EmployeeMessage(BaseModel):
    name: str
    id: int
    content: str = Field(max_length = 15) # min length!
    department: Optional[str] = None
    msg_time: datetime = Field(default_factory=datetime.now)
    

emp_msg1 = EmployeeMessage(
    name="Mustafa Buyukdereli",
    id=101,
    content="Be happy and smile always!",
)

print(emp_msg1)

emp_msg2 = EmployeeMessage(
    name="Bengü Özbilici",
    id=301,
    content="Imm...",
)

print(emp_msg2)

# 1 validation error for EmployeeMessage
# content
# String should have at most 15 characters 

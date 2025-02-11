from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Level(str, Enum):
    D = "Director"
    M = "Manager"
    E = "Expert"
    A = "Assistant"

class EmployeeMessage(BaseModel):
    name: str
    id: int
    title: Level
    content: str
    department: Optional[str] = None
    

emp_msg1 = EmployeeMessage(
    name="Mustafa Buyukdereli",
    id=101,
    title=Level.D,
    content="Be happy!",
)


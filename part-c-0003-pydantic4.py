from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EmployeeMessage(BaseModel):
    name: str
    id: int
    content: str
    department: Optional[str] = None
    msg_time: datetime = Field(default_factory=datetime.now)
    

emp_msg1 = EmployeeMessage(
    name="Mustafa Buyukdereli",
    id=101,
    content="Be happy!",
)

print(emp_msg1)

import time
time.sleep(10)

emp_msg2 = EmployeeMessage(
    name="Bengü Özbilici",
    id=301,
    content="Be careful always!",
)

print(emp_msg2)

# name='Mustafa Buyukdereli' id=101 content='Be happy!' department=None msg_time=datetime.datetime(2025, 2, 11, 23, 42, 51, 980472)
# name='Bengü Özbilici' id=301 content='Be careful always!' department=None msg_time=datetime.datetime(2025, 2, 11, 23, 43, 1, 981095)

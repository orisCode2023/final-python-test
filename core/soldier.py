from pydantic import BaseModel, field_validator
from enum import Enum

class Assign(str, Enum):
    ASSIGNED = "assigned"
    WAITING = "waiting" 

class Soldier(BaseModel):
    personal_number: int
    name : str
    last_name : str
    gender : str
    home_town : str
    base_distence : int
    status_assign : Assign 

    @field_validator('personal_number')
    @classmethod
    def validat_personal_name(cls, pn: int):
        new_pn = str(pn)
        if not new_pn.startswith('8'):
            raise ValueError("The number must start with 8")
    
    

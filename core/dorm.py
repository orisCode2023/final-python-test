from soldier import *
from pydantic import Field

class Room(BaseModel):
    room_number: int 
    soldiers_per_room : list[Soldier] = Field(max_length=8) 


class Dorm(BaseModel):
    dorm_number : int
    rooms : list = Field(max_length=10) 


class Base(BaseModel):
   dorms : list = Field(min_length=2)
    
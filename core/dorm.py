from soldier import *
from pydantic import Field

class Room:
    room_number: int 
    soldiers_per_room : list[Soldier] = Field(max_length=8) 


class Dorm(BaseModel):
    rooms : list[Room] = Field(max_length=10) 


class Base:
   dorms : list[Dorm] = Field(ge=2)
    
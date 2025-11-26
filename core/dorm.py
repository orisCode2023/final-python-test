from soldier import *

class Room:
    room_number: int 
    soldiers_per_room : list[Soldier] = Field(le=8) 

    # @field_validator('soldiers_per_room')
    # @classmethod
    # def validat_personal_name(cls, soldier_number: int):
    #    if soldier_number != 8:
    #        raise

class Dorm(BaseModel):
    rooms : list[Room] = Field(default=2) 




    
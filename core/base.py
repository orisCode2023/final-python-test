from dorm import *
 
class Base:
   dorms : list[Dorm] = Field(ge=2)
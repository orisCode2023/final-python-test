from operator import itemgetter
from dorm import *
from csv_handler import *
class Controller:
    def __init__(self):
        self.room = Room(room_number=1, soldiers_per_room=[])
        self.dorm = Dorm(dorm_number=1, rooms=[])
        self.base = Base(dorms=[Dorm, Dorm])


    def sort_by_distance(self):
        with open('data.csv') as f:
            data = read_csv(f)
        sorted_list = sorted(data, key=itemgetter('distance'), reverse=True)
        return sorted_list


    def create_soldier(self):
        for soldier in self.sort_by_distance():
            soldier_instance = Soldier(
                personal_number=int(soldier['soldier_number']),
                name=soldier['first_name'],                              
                last_name=soldier['last_name'], 
                gender=soldier['gender'],
                home_town=soldier['city'],
                base_distence=int(soldier['distance']),
                status_assign=Assign.WAITING)
        
        return soldier_instance
                
    def update_soldier(self):
        soldier = self.create_soldier()
        soldier.room_number = self.room.room_number
        soldier.dorm_number = self.dorm.dorm_number
        soldier.status_assign = Assign.ASSIGNED      
        return soldier                                  


    def assign_soldiers(self):
        waiting_list = []
        assign_soldeiers_counter = 0
        final_update_soldier = []
        for i in range(len(self.sort_by_distance())):
            soldier = self.update_soldier()
            if self.dorm.dorm_number > 2:
                waiting_list.append(soldier)
            
            else:
                self.room.soldiers_per_room.append(soldier)
                assign_soldeiers_counter += 1


                if len(self.room.soldiers_per_room) - 1 == 7:
                    self.dorm.rooms.append(self.room.soldiers_per_room)
                    self.room.soldiers_per_room = []
                    self.room.room_number += 1

                    if len(self.dorm.rooms)- 1 == 9:
                        self.base.dorms.append(self.dorm.rooms)
                        self.dorm.rooms = []
                        self.dorm.dorm_number += 1

            final_update_soldier.append(soldier)


            

        return {"waiting_list": len(waiting_list), "assigned" : assign_soldeiers_counter, "soldiers": final_update_soldier}
        

    # def get_spesific_soldier_values(self):
    #     lst = self.assign_soldiers['soldiers']
    #     for soldier in lst:
    #         print(soldier['personal_number'])
    #         print(soldier['status_assign'])
    #         print(soldier['room_number'])
    #         print(soldier['dorm_number'])
            
            

con = Controller()
print(con.get_spesific_soldier_values())


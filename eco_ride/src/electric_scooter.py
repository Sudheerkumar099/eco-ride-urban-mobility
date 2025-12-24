from vehicle import Vehicle
class ElectricScooter(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit):
        super().__init__(vehicle_id,model,battery_percentage)
        if(max_speed_limit>=0):
            self.max_speed_limit=max_speed_limit
        else:
            raise Exception("speed should be greater that 0")
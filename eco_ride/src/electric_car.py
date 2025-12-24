from vehicle import Vehicle
class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        if seating_capacity>0:
            self.seating_capacity=seating_capacity
        else :
            raise Exception("seating capacity should be grater than zero")
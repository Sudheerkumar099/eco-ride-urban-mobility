from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = None
        self.set_battery_percentage(battery_percentage)

        self.__maintenance_status="Available"
        self.__rental_price = 100
    
    def get_battery_percentage(self):
        return self.__battery_percentage
    
    def set_battery_percentage(self,battery_percentage):
        if battery_percentage <= 100 and battery_percentage >=0 :
            self.__battery_percentage = battery_percentage
        else:
            raise ValueError
    
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_maintenance_status(self,maintenance_status):
        self.__maintenance_status=maintenance_status

    def get_rental_price(self):
        return self.__rental_price
    
    def set_rental_price(self,rental_price):
        if rental_price >= 0:
            self.__rental_price=rental_price  
        else:
           raise ValueError
    
    def __eq__(self,other) :
        if isinstance(other,Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False      

    def __str__(self):
        return (f"{type(self)} ID: {self.vehicle_id} Model: {self.model} Battery Percentage: {self.get_battery_percentage()}%")
   
    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass
    '''child class must implement'''


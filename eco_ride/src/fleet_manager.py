from electric_scooter import ElectricScooter
from electric_car import ElectricCar
class Fleetmanager:
    def __init__(self):
        self.hubs={}
    
    def add_hub(self):
        hub_name = input("Please Enter the hub name :\n") 
        if hub_name in self.hubs:
            print("hub Already exsits")
        else:
            self.hubs[hub_name]=[]
            print(f"{hub_name} added Sucessfully")
    
    def add_vehicle_to_hub(self):
        hub_name = input("Enter the Hub name to Add Vehicle to Hub:\n")

        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exsist")
            return

        option = input("Select the vehicle you want to add :\nEnter 1 for Electric Scooter \nEnter 2 for Electric Car\n")
        print("Enter 1 for Electric Scooter \n Enter 2 for Electric Car")
        vehicle = None
        id = input("Enter the id of the Vehicle:\n")
        model = input("Enter the model of the vehicle:\n")
        battery_percentage = int(input("Enter the battery percentage:\n"))

        if option == "1":
            max_speed= int(input("Enter the max Speed of the vehicle\n"))
            vehicle = ElectricScooter(id,model,battery_percentage,max_speed)

        elif option == "2":
            max_capacity = int(input("Enter the max Speed of the vehicle"))
            vehicle = ElectricCar(id,model,battery_percentage,max_capacity)
        else:
            print("Invalid option")
            return
        
        existing_vehicles = self.hubs[hub_name]
        duplicates = [i for i in existing_vehicles if i == vehicle]

        if duplicates:
            print(f"a vehicle with {vehicle.vehicle_id} id  already exists in the {hub_name} hub")
            return

        self.hubs[hub_name].append(vehicle)
        print("vehicle added success fully")
        print(self.hubs)    

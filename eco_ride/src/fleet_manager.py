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
        option = input("Select the vehicle you want to add :\nEnter 1 for Electric Scooter \nEnter 2 for Electric Car\n")
        print("Enter 1 for Electric Scooter \n Enter 2 for Electric Car")
        vehicle = None
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exsist")
        else:
            if option == "1":
                id = input("Enter the id of the Vehicle:\n")
                model = input("Enter the model of the vehicle:\n")
                battery_percentage = int(input("Enter the battery percentage:\n"))
                max_speed= int(input("Enter the max Speed of the vehicle"))
                vehicle = ElectricScooter(id,model,battery_percentage,max_speed)
            elif option == "2":
                id = input("Enter the id of the Vehicle:\n")
                model = input("Enter the model of the vehicle:\n")
                battery_percentage = int(input("Enter the battery percentage:\n"))
                max_capacity = int(input("Enter the max Speed of the vehicle"))
                vehicle = ElectricCar(id,model,battery_percentage,max_capacity)

            self.hubs[hub_name].append(vehicle)
            print("vehicle added success fully")
            print(self.hubs)
    
    def add_multiple_vehicles_to_hub(self):
        hub_name = input("Enter the Hub name to Add Vehicle to Hub:\n")
        vehicle = None
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exsist")
        else:
            for i in range(int(input("Enter the number of vehicles\n"))):
                option = input("Select the vehicle you want to add :\nEnter 1 for Electric Scooter \nEnter 2 for Electric Car\n")
                if option == "1":
                    id = input("Enter the id of the Vehicle:\n")
                    model = input("Enter the model of the vehicle:\n")
                    battery_percentage = int(input("Enter the battery percentage:\n"))
                    max_speed= int(input("Enter the max Speed of the vehicle"))
                    vehicle = ElectricScooter(id,model,battery_percentage,max_speed)
                elif option == "2":
                    id = input("Enter the id of the Vehicle:\n")
                    model = input("Enter the model of the vehicle:\n")
                    battery_percentage = int(input("Enter the battery percentage:\n"))
                    max_capacity = int(input("Enter the max Speed of the vehicle"))
                    vehicle = ElectricCar(id,model,battery_percentage,max_capacity)
                self.hubs[hub_name].append(vehicle)
                print("vehicle added success fully")
                print(self.hubs)
        

from electric_scooter import ElectricScooter
from electric_car import ElectricCar
class Fleetmanager:
    def __init__(self):
        self.hubs={"airport":[ElectricScooter(123,"ather",9,100),ElectricScooter(124,"ola",8,100),ElectricCar(125,"bmw",90,4)]}
    
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

    def search_vehicles_by_hub(self):
        hub_name = input("Enter the name of the hub to get vehicle details:\n")
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist.")
            return
        vehicles = self.hubs[hub_name]

        if not vehicles:
            print(f"No vehicles are present in the hub {hub_name}")
            return
        
        for v in vehicles:
            v.display_details()

    def search_by_battery_percent(self):
        hub_name = input("Enter the Hub name To get the Vehicle\n")
        if hub_name not in self.hubs:
            print(f"{hub_name} does not exist in the Hubs")
            return
        vehicles = self.hubs[hub_name]

        high_battery = list(filter(lambda v : v.get_battery_percentage() > 80, vehicles))

        if not high_battery:
            print(f"No vehicles found with battery greater that 80% in {hub_name}")
            return

        for v in high_battery :
            v.display_details()
            
    def categorized_view(self):
        vehicles_dict = {"Electric Cars":[],"Electric Scooters":[]}

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                if isinstance(vehicle,ElectricCar):
                    vehicles_dict["Electric Cars"].append(vehicle)
                elif isinstance(vehicle,ElectricScooter):
                    vehicles_dict["Electric Scooters"].append(vehicle)
        
        for vehicle_type, vehicles in vehicles_dict.items():
            print(f"\n{vehicle_type}")
            if not vehicles:
                print("No vehicles are present")
            else:
                for v in vehicles:
                    v.display_details()
    
    def status_analytics(self):
        status_count = {"Available":0,"On Trip":0,"Under Maintenance":0}
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in status_count:
                    status_count[status]+=1
        print(f"Available vehicles            : {status_count["Available"]}")
        print(f"On Trip vehicles              : {status_count["On Trip"]}")
        print(f"Under Maintenance vehicles    : {status_count["Under Maintenance"]}")
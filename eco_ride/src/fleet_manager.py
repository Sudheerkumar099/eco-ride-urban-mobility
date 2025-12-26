import json
import csv
from electric_scooter import ElectricScooter
from electric_car import ElectricCar
class Fleetmanager:
    def __init__(self):
        self.hubs={"airport":[ElectricScooter(123,"ather",9,100),ElectricScooter(124,"ola",8,100),ElectricCar(125,"bmw",90,4)]}

        self.hubs["airport"][2].set_rental_price(300)
    
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
        vehicle = None
        id = input("Enter the id of the Vehicle:\n")
        model = input("Enter the model of the vehicle:\n")
        battery_percentage = int(input("Enter the battery percentage:\n"))

        if option == "1":
            max_speed= int(input("Enter the max Speed of the vehicle\n"))
            vehicle = ElectricScooter(id,model,battery_percentage,max_speed)

        elif option == "2":
            max_capacity = int(input("Enter the max capacity of the vehicle\n"))
            vehicle = ElectricCar(id,model,battery_percentage,max_capacity)
        else:
            print(f"Invalid option {option} does not Exist")
            return
        
        existing_vehicles = self.hubs[hub_name]
        duplicates = [i for i in existing_vehicles if i == vehicle]

        if duplicates:
            print(f"a vehicle with {vehicle.vehicle_id} id  already exists in the {hub_name} hub")
            return

        self.hubs[hub_name].append(vehicle)
        print("vehicle added success fully")
        # print(self.hubs)    

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
        status_count = {"available":0,"on trip":0,"under maintenance":0}
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in status_count:
                    status_count[status]+=1
        print(f"Available vehicles            : {status_count["available"]}")
        print(f"On Trip vehicles              : {status_count["on trip"]}")
        print(f"Under Maintenance vehicles    : {status_count["under maintenance"]}")

    def sort_by_model(self):

        hub_name = input("Enter the hub name to sort Vehicles:\n")

        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist")
            return
        vehicles = self.hubs[hub_name]

        if not vehicles:
            print(f"No vehicles are present in the Hub")
            return

        sorted_vehicles = []

        for v in vehicles:
            sorted_vehicles.append(v.model.lower())
        sorted_vehicles.sort()

        print(f"These are the vehicle models from {hub_name}")
        
        for v in sorted_vehicles:
            for i in vehicles:
                if v == i.model:
                    i.display_details()

    def sort_by_battery(self):
        hub_name = input("Enter the hub name to sort Vehicles:\n")

        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist")
            return
        vehicles = self.hubs[hub_name]
        if not vehicles:
            print(f"No vehicles are present in the Hub")
            return
        sorted_vehicles = sorted(vehicles,key = lambda v: v.get_battery_percentage(),reverse=True)

        for v in sorted_vehicles:
            v.display_details()

    def sort_by_fare(self):
        hub_name = input("Enter the hub name to sort Vehicles:\n")

        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist")
            return
        vehicles = self.hubs[hub_name]
        if not vehicles:
            print(f"No vehicles are present in the Hub")
            return
        sorted_vehicles = sorted(vehicles,key = lambda v: v.get_rental_price(),reverse=True)

        for v in sorted_vehicles:
            v.display_details()
            print(f"Rental price: {v.get_rental_price()}")

    def save_to_csv(self,filename="fleet_data.csv"):
        with open(filename,mode="w",newline="")as file:
            writer = csv.writer(file)

            writer.writerow(["hub_name","vehicle_type","vehicle_id","model","battery","extra"])
            for hub_name,vehicles in self.hubs.items():
                for vehicle in vehicles:
                    if isinstance(vehicle, ElectricCar):
                        writer.writerow([hub_name,"ElectricCar",vehicle.vehicle_id,vehicle.model,vehicle.get_battery_percentage(),vehicle.seating_capacity])
                    elif isinstance(vehicle, ElectricScooter):
                        writer.writerow([hub_name,"ElectricScooter",vehicle.vehicle_id,vehicle.model,vehicle.get_battery_percentage(),vehicle.max_speed_limit])
        print(f"Fleet data saved to CSV successfully to {filename}")
    
    def load_from_csv(self, filename="fleet_data.csv"):
        try:
            with open(filename,mode="r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    hub_name = row["hub_name"]

                    if hub_name not in self.hubs:
                        self.hubs[hub_name]=[]

                    if row["vehicle_type"] == "ElectricCar":
                        vehicle = ElectricCar(row["vehicle_id"],row["model"],int(row["battery"]),int(row["extra"]))
                    elif row["vehicle_type"] == "ElectricScooter":
                        vehicle = ElectricScooter(row["vehicle_id"],row["model"],int(row["battery"]),int(row["extra"]))
                    self.hubs[hub_name].append(vehicle)
                print(f"Data loaded from {filename} successfully")
                    
        except:
            print("File not Found")

    def save_to_json(self,file_name="fleet_data.json"):
        data={}

        for hub_name,vehicles in self.hubs.items():
            data[hub_name]=[]
            for vehicle in vehicles:
                if isinstance(vehicle, ElectricCar):
                    data[hub_name].append({"type":"ElectricCar","vehicle_id":vehicle.vehicle_id,"model":vehicle.model,"battery": vehicle.get_battery_percentage(),"extra": vehicle.seating_capacity})
                elif isinstance(vehicle,ElectricScooter):
                    data[hub_name].append({"type":"ElectricScooter","vehicle_id":vehicle.vehicle_id,"model":vehicle.model,"battery":vehicle.get_battery_percentage(),"extra":vehicle.max_speed_limit})
        with open(file_name,"w") as file:
            json.dump(data,file,indent=4)
        
        print("Fleet data saved to JSON successfully")
    
    def load_from_json(self,file_name="fleet_data.json"):
        try:
            with open(file_name,"r") as file:
                data = json.load(file)
            
            for hub_name , vehicles in data.items():
                self.hubs[hub_name]=[]

                for v in vehicles:
                    if v["type"] == "ElectricCar": 
                        vehicle = ElectricCar(v["vehicle_id"],v["model"],v["battery"],v["extra"])
                    elif v["type"] == "ElectricScooter": 
                        vehicle = ElectricScooter(v["vehicle_id"],v["model"],v["battery"],v["extra"])
                    
                    self.hubs[hub_name].append(vehicle)
            print("Fleet data loaded from JSON")
            print(self.hubs)
        except:
            print(f"Json file {file_name} not found")
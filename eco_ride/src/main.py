from electric_scooter import ElectricScooter
from electric_car import ElectricCar
from fleet_manager import Fleetmanager
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

    def main():
        EcoRideMain.greet()
        fm = Fleetmanager()
        lst = fm.hubs["airport"]
        lst[2].set_maintenance_status("On Trip")
        lst[1].set_maintenance_status("Under Maintenance")
        fm.status_analytics()
    
if __name__ == "__main__" :
   EcoRideMain.main()
    
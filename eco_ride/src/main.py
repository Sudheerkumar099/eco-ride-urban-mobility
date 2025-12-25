from electric_scooter import ElectricScooter
from electric_car import ElectricCar
from fleet_manager import Fleetmanager
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

    def main():
        EcoRideMain.greet()
        fm = Fleetmanager()
        fm.load_from_csv()
    
if __name__ == "__main__" :
   EcoRideMain.main()
    
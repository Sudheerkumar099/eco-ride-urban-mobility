from electric_scooter import ElectricScooter
from electric_car import ElectricCar
from fleet_manager import Fleetmanager
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

    def main():
        EcoRideMain.greet()
        ather = ElectricScooter(123,"ather",90,100)
        ola = ElectricScooter(124,"ola",80,100)
        car = ElectricCar(125,"bmw",90,4)
        fm = Fleetmanager()
        fm.add_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
    

if __name__ == "__main__" :
   EcoRideMain.main()
    
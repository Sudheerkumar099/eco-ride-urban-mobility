from electric_scooter import ElectricScooter
from electric_car import ElectricCar
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

if __name__ == "__main__" :
    EcoRideMain.greet()
    e = ElectricScooter(123,"ather",90,100)
    print(e.max_speed_limit)
    c = ElectricCar(1,"bmw",90,4)
    print(c.seating_capacity)
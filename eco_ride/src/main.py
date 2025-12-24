from electric_scooter import ElectricScooter
from electric_car import ElectricCar
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

    def main():
        EcoRideMain.greet()
    ather = ElectricScooter(123,"ather",90,100)
    ola = ElectricScooter(124,"ola",80,100)
    car = ElectricCar(125,"bmw",90,4)
    lst = [ather,car,ola]
    for i in lst:
        print(i.calculate_trip_cost(50))

if __name__ == "__main__" :
   EcoRideMain.main()
    
from vehicle import *
class EcoRideMain :
    def greet():
        print("Welcome to Eco-Ride Urban Mobility System")

if __name__ == "__main__" :
    EcoRideMain.greet()
    v= Vehicle(123,"bmw",100)
    print(v.get_battery_percentage())
    v.set_maintenance_status("all good")
    print(v.get_maintenance_status())
    v.set_rental_price(50)
    print(v.get_rental_price())

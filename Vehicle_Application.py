class Vehicle_system:
    def __init__(self,name,fuel_type,brand):
        self.name = name
        self.fuel_type = fuel_type
        self.brand = brand
    def start_engine(self):
        print("Engine started....")
    def stop_engine(self):
        print("Engine stopped....")
class Car(Vehicle_system):
    def __init__(self,brand):
        super().__init__("Car","Diesel",brand)
    def play_music(self):
        print("Music Playing....")
    def open_trunk(self):
        print("Trunk Opened....")
        
class Bike(Vehicle_system):
    def __init__(self,brand):
        super().__init__("Bike","Petrol",brand)
    def kick_start(self):
        print("Bike started....")
    def wheelie(self):
        print("Doing Wheelie...")
vehicle_system = Car("Kia")
vehicle_system.play_music()
vehicle_system.open_trunk()
print(vehicle_system.name,vehicle_system.fuel_type,vehicle_system.brand,sep="\n")
print()
vehicle_system = Bike("Royal_Enfield")
vehicle_system.kick_start()
vehicle_system.wheelie()
print(vehicle_system.name,vehicle_system.fuel_type,vehicle_system.brand,sep="\n") 

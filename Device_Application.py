title = Device Application 
print(title)
class Device:
    def __init__(self, brand, power_status):
        self.brand = brand
        self.power_status = power_status
    def turn_on(self):
        print("Device is turned ON")
    def turn_off(self):
        print("Device is turned OFF")
class Computer(Device):
    def __init__(self, brand, power_status, ram):
        super().__init__(brand, power_status)
        self.ram = ram
    def run_program(self):
        print("Program is running")
class Laptop(Computer):
    def __init__(self, brand, power_status, ram, battery):
        super().__init__(brand, power_status, ram)
        self.battery = battery
    def check_battery(self):
        print("Battery is good")
class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    def capture_image(self):
        print("Image captured")
class SmartLaptop(Laptop, Camera):
    def __init__(self, brand, power_status, ram, battery, megapixels):
        Laptop.__init__(self, brand, power_status, ram, battery)
        Camera.__init__(self, megapixels)
    def show_details(self):
        print("Brand:", self.brand)
        print("Power Status:", self.power_status)
        print("RAM:", self.ram)
        print("Battery:", self.battery)
        print("Megapixels:", self.megapixels)
obj = SmartLaptop("MAC", "ON", "16GB", "5000mAh", "48MP")
obj.turn_on()
obj.run_program()
obj.check_battery()
obj.capture_image()
obj.show_details()
obj.turn_off()

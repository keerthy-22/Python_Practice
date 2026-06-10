class Laptop:
    def __init__(self,brand_name,os,ram,processor,rom,display_size):
        self.brand_name = brand_name
        self.os = os
        self.ram = ram
        self.processor = processor
        self.rom = rom
        self.diplay_size = display_size
    def typing(self):
        print("typing.....")
    def charging(self):
        print("charging.....")
    def shutdown(self):
        print("shutdown.....")
class MAC(Laptop):
    def __init__(self,ram,processor,rom,display_size):
        super().__init__("Apple","MAC OS",ram,processor,rom,display_size)
    def beautify(self):
        print("Beautify")

laptop = MAC("16 GB","M3","256 GB","13.6-inch")
laptop.typing()
print(laptop.os,laptop.ram,laptop.brand_name,laptop.rom)
laptop.charging
    
    
    

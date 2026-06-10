class FaceWash:
    def __init__(self,brand_name,type_of_skin):
        self.brand_name = brand_name
        self.type_of_skin = type_of_skin
    
    def foam(self):
        print("Foam has been generated")
    
    def remove_dullness(self):
        print("Dullness has been removed")
        
    def remove_dryness(self):
        print("Dryness removed")
        
class HyphenFaceWash(FaceWash):
    def __init__(self,type_of_skin):
        super().__init__("Hyphen",type_of_skin)
        
    def add_glow(self):
        print("Glow added")
    
facewash = HyphenFaceWash("All skin type")
facewash.foam()
facewash.remove_dullness()
facewash.remove_dryness()
facewash.add_glow()

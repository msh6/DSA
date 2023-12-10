class Flower:
    
    def __init__(self, name=str, petals=int, price=float):
        self.name = name
        self.petals = petals
        self.price = price
        
    def set_name(self, name: str):
        self.name = name
        
    def set_petals(self, petals: str):
        self.petals = petals
        
    def set_price(self, price: str):
        self.price = price
        
    def get_name(self) -> str:
        return self.name
    
    def get_petals(self) -> int:
        return self.petals
    
    def get_price(self) -> float:
        return self.price
    
lily = Flower("Lily", 10, 12.50)
print("Name: ", lily.get_name())
print("Petals: ", lily.get_petals())
print("Price: ", lily.get_price())

rose = Flower()
rose.set_name("Rose")
rose.set_petals(25)
rose.set_price(18.50)
print("Name: ", rose.get_name())
print("Petals: ", rose.get_petals())
print("Price: ", rose.get_price())


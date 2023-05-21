from restaurant import restaurant

class HomeKitchen(restaurant):
    def __init__(self, name, capacity, size, stove_type, hood_name):
        super().__init__(name, capacity, size)
        self.stove_type = stove_type
        self.hood_name = hood_name
    
    def add_guests(self, guests):
        print("Cannot add guests. It's a home kitchen.")
    
    def kitchen_type(self):
        return "Home kitchen"
    
    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Size: {self.size}, Stove Type: {self.stove_type}, Hood Name: {self.hood_name}"






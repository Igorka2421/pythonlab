"""
In this class i create object
"""
from abstract_kitchen import AbstractKitchen
class Restaurant(AbstractKitchen):
    def __init__(self, name, year_of_foundation, max_capacity, rating, opening_time, closing_time):
        super().__init__(name, max_capacity, rating)
        self.year_of_foundation = year_of_foundation
        self.max_capacity = max_capacity
        self.rating = rating
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.current_capacity = 0
    
    def add_guests(self, guests):
        if self.current_capacity + guests > self.max_capacity:
            print("Cannot add guests. The restaurant is full.")
        else:
            self.current_capacity += guests
    
    def kitchen_type(self):
        return "Restaurant kitchen"
    
    def do_something(self):
        return f"Do something in {self.name}"
    
    def __str__(self):
        return f"Name: {self.name}, Year of Foundation: {self.year_of_foundation}, Max Capacity: {self.max_capacity}, Rating: {self.rating}, Opening Time: {self.opening_time}, Closing Time: {self.closing_time}, Current Capacity: {self.current_capacity}"


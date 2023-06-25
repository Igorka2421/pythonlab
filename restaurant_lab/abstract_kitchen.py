from abc import ABC, abstractmethod

class AbstractKitchen(ABC):
    def __init__(self, name, capacity, size):
        self.name = name
        self.capacity = capacity
        self.size = size
    
    @abstractmethod
    def add_guests(self, guests):
        pass
    
    @abstractmethod
    def kitchen_type(self):
        pass
    
    def do_something(self):
        pass


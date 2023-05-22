"""
The 'HomeKitchen' module defines the 'HomeKitchen' class representing a home kitchen.

The 'HomeKitchen' class is derived from the 'restaurant' class and provides a way to model
and manage a home kitchen. It includes attributes such as the name, capacity, size, stove type,
and hood name of the kitchen, as well as methods for retrieving the kitchen type.

Module Contents:
- HomeKitchen: A class representing a home kitchen.

"""

from restaurant import Restaurant

class HomeKitchen(Restaurant):
    """
    A class representing a home kitchen, derived from the 'restaurant' class.

    Methods:
    - __init__(self, name="", capacity=0, size=0, stove_type="", hood_name=""): 
    Initializes a new HomeKitchen instance.

    """
    #pylint:disable=too-many-arguments
    def __init__(self, name="", capacity=0, year_of_foundation= 0,
                 size=0, rating =0, stove_type="",
                 opening_time = 0, closing_time = 0, hood_name=""):
        """
        Initializes a new HomeKitchen instance.

        Args:
            name (str): The name of the home kitchen.
            capacity (int): The maximum capacity of the home kitchen.
            size (int): The size of the home kitchen.
            stove_type (str): The type of stove in the home kitchen.
            hood_name (str): The name of the hood in the home kitchen.

        Returns:
            None

        Raises:
            None
        """
        super().__init__(name, year_of_foundation, capacity, rating, opening_time, closing_time)
        self.capacity = capacity
        self.size = size
        self.stove_type = stove_type
        self.hood_name = hood_name

    def add_guests(self, guests):
        """
        in this method we check if we can add a guest to this class
        """
        if self.current_capacity + guests > self.max_capacity:
            print("Cannot add guests. The restaurant is full.")
        else:
            self.current_capacity += guests

    def kitchen_type(self):
        """
           Returns the type of stove in the home kitchen.
        """
        return "Home kitchen"

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Size: {self.size},"\
           f"Stove Type: {self.stove_type}, Hood Name: {self.hood_name}"

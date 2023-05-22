"""
In this class i create object
"""

from abc import ABC, abstractmethod

class Restaurant(ABC):
    """
    A class representing a restaurant.

    """
    #pylint:disable=too-many-arguments
    def __init__(self, name, year_of_foundation, max_capacity, rating, opening_time, closing_time):
        """
        Initialize a Restaurant object.

        Args:
            name (str): The name of the restaurant.
            year_of_foundation (int): The year the restaurant was founded.
            max_capacity (int): The maximum capacity of the restaurant.
            rating (float): The rating of the restaurant.
            opening_time (str): The opening time of the restaurant.
            closing_time (str): The closing time of the restaurant.

        """
        self.name = name
        self.year_of_foundation = year_of_foundation
        self.max_capacity = max_capacity
        self.rating = rating
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.current_capacity = 0


    def add_guests(self, guests):
        """
        Add guests to the restaurant.

        Args:
            guests (int): The number of guests to add.

        Returns:
            None

        Raises:
            None
        """
        if self.current_capacity + guests > self.max_capacity:
            print("Cannot add guests. The restaurant is full.")
        else:
            self.current_capacity += guests
    @abstractmethod
    def kitchen_type(self):
        """
        Abstract method to be implemented by subclasses.
        Returns the type of kitchen in the restaurant.

        Args:
            None

        Returns:
            str: The type of kitchen in the restaurant.

        Raises:
            None
        """
        return "Restaurant kitchen"

    def __str__(self):
        return f"Name: {self.name}, Year of Foundation: {self.year_of_foundation},"\
           f"Max Capacity: {self.max_capacity},"\
           f"Rating: {self.rating}, Opening Time: {self.opening_time},"\
           f"Closing Time: {self.closing_time}, Current Capacity: {self.current_capacity}"

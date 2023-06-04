"""
In this class i initialize a Restaurant object
"""
from distutils.command.check import check
import logging
from home_kitchen import HomeKitchen

class KitchenManager:
    """
    A class representing a kitchen manager.
    Methods:
        __init__():
            Initializes a new instance of the KitchenManager class.
        add_kitchen(kitchen):
            Adds a kitchen to the manager.
        display_kitchens():
            Displays the list of kitchens managed by the manager.
    """
    def __init__(self):
        """
        Initializes a new instance of the KitchenManager class.
        """
        self.kitchens = []

    def add_kitchen(self, kitchen):
        """
        Adds a kitchen to the manager.
        Parameters:
            kitchen (HomeKitchen): The kitchen to be added.
        """
        self.kitchens.append(kitchen)

    def display_kitchens(self):
        """
        Displays the list of kitchens managed by the manager.
        """
        for kitchen in self.kitchens:
            print(kitchen)

    def logged(exception, mode):
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    if mode == "console":
                        logging.error(str(e))
                    elif mode == "file":
                        logging.basicConfig(filename="log.txt", level=logging.ERROR)
                        logging.error(str(e))
                    else:
                        raise ValueError("Invalid logging mode")

            return wrapper
        return decorator

    @logged(check, mode="console")
    def rating(self):

        pass

if __name__ == "__main__":
    manager = KitchenManager()

    home_kitchen = HomeKitchen("My Kitchen", 5, "Small", "Electric", "ABC Hood")

    manager.add_kitchen(home_kitchen)

    manager.display_kitchens()

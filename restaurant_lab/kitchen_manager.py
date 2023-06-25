from restaurant import Restaurant
from home_kitchen import HomeKitchen

class KitchenManager:
    def __init__(self):
        self.kitchens = []
    
    def add_kitchen(self, kitchen):
        self.kitchens.append(kitchen)
    
    def display_kitchens(self):
        for kitchen in self.kitchens:
            print(kitchen)
    
    def __len__(self):
        return len(self.kitchens)
    
    def __getitem__(self, index):
        return self.kitchens[index]
    
    def __iter__(self):
        return iter(self.kitchens)
    
    def get_do_something_results(self):
        results = [kitchen.do_something() for kitchen in self.kitchens]
        return results
    
    def get_enumerated_kitchens(self):
        enumerated_kitchens = [(i, kitchen) for i, kitchen in enumerate(self.kitchens)]
        return enumerated_kitchens
    
    def get_zipped_results(self):
        results = [kitchen.do_something() for kitchen in self.kitchens]
        zipped_data = zip(self.kitchens, results)
        return zipped_data
    
    def get_attributes_by_type(self, attribute_type):
        attributes = {key: value for key, value in self.kitchens[0].__dict__.items() if isinstance(value, attribute_type)}
        return attributes
    
    def check_conditions(self, condition):
        result = {"all": all(condition(kitchen) for kitchen in self.kitchens),
                  "any": any(condition(kitchen) for kitchen in self.kitchens)}
        return result

if __name__ == "__main__":
    manager = KitchenManager()
    
    restaurant = Restaurant("Victor's Restaurant", 2000, 100, 4.5, "08:00", "22:00")
    home_kitchen = HomeKitchen("My Kitchen", 5, "Small", "Electric", "ABC Hood")
    
    manager.add_kitchen(restaurant)
    manager.add_kitchen(home_kitchen)
    
    manager.display_kitchens()
    
    results = manager.get_do_something_results()
    print(results)
    
    enumerated_kitchens = manager.get_enumerated_kitchens()
    print(enumerated_kitchens)
    
    zipped_data = manager.get_zipped_results()
    for kitchen, result in zipped_data:
        print(kitchen, result)

    attributes = manager.get_attributes_by_type(int)
    print(attributes)

    condition = lambda kitchen: kitchen.capacity > 10
    condition_result = manager.check_conditions(condition)
    print(condition_result)

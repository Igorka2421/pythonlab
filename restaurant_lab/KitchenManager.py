from restaurant import Restaurant
from HomeKitchen import HomeKitchen

class KitchenManager(Restaurant, HomeKitchen):
    
    def main():
        restaurants = [Restaurant("Victor's Restaurant", 2000, 100, 4.5, "08:00", "22:00"),
                       HomeKitchen("s", "v")]

        for restaurant in restaurants:
            print(restaurant)

if __name__ == "__main__":
    KitchenManager.main()



class Restaurant:
    def __init__(self, name="", rating=0, max_capacity=0, current_capacity=0):
        self.name = name
        self.rating = rating
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

    def acceptReservation(self, num_of_guests):
        if self.current_capacity + num_of_guests > self.max_capacity:
            return False
        else:
            self.current_capacity += num_of_guests
            return True

    def removeReservation(self, num_of_guests):
        if self.current_capacity - num_of_guests < 0:
            return False
        else:
            self.current_capacity -= num_of_guests
            return True

    staticmethod
    def getInstence():
        Instence = Restaurant()

    def __str__ (self):
        return f"name: {self.name}, Rating: {self.rating}, max_capacity:" 
        f"{self.max_capacity}, current_capacity: {self.current_capacity}"

if __name__ == "__main__":
    restaurant = Restaurant("Victor", 5, 100, 54)

    print(restaurant.acceptReservation(5))  
    print(restaurant.removeReservation(5))  


    restaurants = []

    restaurants.append(Restaurant())
    restaurants.append(Restaurant("Victo", 5, 100, 54))
    restaurants.append(Restaurant())
    restaurants.append(Restaurant())

    for restaurant in restaurants:
        print(restaurant)



      
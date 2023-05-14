class Restaurant:
    def __init__(self, name="", rating=0, maxCapacity=0, currentCapacity=0):
        self.name = name
        self.rating = rating
        self.maxCapacity = maxCapacity
        self.currentCapacity = currentCapacity

    def acceptReservation(self, numOfGuests):
        if self.currentCapacity + numOfGuests > self.maxCapacity:
            return False
        else:
            self.currentCapacity += numOfGuests
            return True

    def removeReservation(self, numOfGuests):
        if self.currentCapacity - numOfGuests < 0:
            return False
        else:
            self.currentCapacity -= numOfGuests
            return True

if __name__ == "__main__":
    restaurant = Restaurant("Victor", 5, 100, 54)

    print(restaurant.acceptReservation(5))  
    print(restaurant.removeReservation(5))  
     

    restaurants = []

    restaurants.append(Restaurant())
    restaurants.append(Restaurant("Victor", 5, 100, 54))
    restaurants.append(Restaurant())
    restaurants.append(Restaurant())

    for restaurant in restaurants:
        print(restaurant)

      
class RestaurantNew:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Welcome to " + self.name)

class IceCreamStand(RestaurantNew):
    def __init__(self, name):
        super().__init__(name)
        self.flavours = {
            "Pista" : "100Rs",
            "Chocolate" : "150Rs",
            "Vanilla" : "250Rs"
        }
        self.working_hours_start = "2pm"
        self.working_hours_end = "9pm"

    def displayFlavours(self):
        for flavour, price in self.flavours.items():
            print(flavour + " is " + price)

    def OpenOrClosedRestuarnt(self,time):
        self.time = time

        if(time >= self.working_hours_start and time <= self.working_hours_end):
            print("Restuarnt Is Open!")

        else:
            print('Resturant Is closed')

class PizzaStand(RestaurantNew):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.flavours = {
            "Tikka" : 1000,
            "Chicken Fajita" : 1600,
            "Supreme" :  2000
        }
        

    def displayFlavours(self):
        for flavour, price in self.flavours.items():
            print(flavour + " is " + str(price) + " Rs")

    

        

# iceCream = IceCreamStand("Baskin Robbins")
# iceCream.greet()
# iceCream.displayFlavours()

iceCream = IceCreamStand("Baskin Robbins")
iceCream.greet()
iceCream.displayFlavours()
iceCream.OpenOrClosedRestuarnt("1am")
class Vechile:
    def __init__(self, wheel):
        self.wheel = wheel


class Car(Vechile):
    def __init__(self, brand, wheel):
        super().__init__(wheel)
        self.brand = brand
    
    def car_brand(self):
        print(self.brand)
    
    def wheel_count(self):
        print(self.wheel)

car1 = Car("Benz", 4)
car1.car_brand()
car1.wheel_count()

car2 = Car("BMW", 2)
car2.car_brand()
car2.wheel_count()
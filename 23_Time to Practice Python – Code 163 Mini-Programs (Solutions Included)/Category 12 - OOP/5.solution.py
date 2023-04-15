class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


school_bus = Bus("Benz", 110, 11)
print(school_bus.color, school_bus.name,
      school_bus.max_speed, school_bus.mileage)

car = Car("Lambo", 380, 11)
print(car.color, car.name, car.max_speed, car.mileage)

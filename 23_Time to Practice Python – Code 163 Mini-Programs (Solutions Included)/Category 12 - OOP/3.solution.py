class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("Some Bus", 150, 12)
print(school_bus.name, school_bus.max_speed, school_bus.mileage)

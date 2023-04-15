class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


some_model = Vehicle(220, 15)
print(some_model.max_speed, some_model.mileage)

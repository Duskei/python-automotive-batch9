class Car:
    # Class attribute: shared by all instances of this class
    wheels = 4

    # The __init__ method is a constructor, automatically called when a new object is created
    def __init__(self, brand, color):
        # Instance attributes: unique to each object
        self.brand = brand
        self.color = color

    # Instance method: defines a behavior for the object
    def display_info(self):
        return f"This {self.color} {self.brand} has {self.wheels} wheels."

# Create objects (instances) from the Car class
car1 = Car("Toyota", "blue")
car2 = Car("Honda", "red")

# Access attributes and call methods using the objects
print(car1.display_info())
print(car2.display_info())  
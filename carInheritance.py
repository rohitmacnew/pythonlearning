class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")


class SportsCar(Car):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed
    
    def drive(self):
        print(f"The {self.make} {self.model} is racing with a top speed of {self.top_speed} mph.")
        

class SUV(Car):
    def __init__(self, make, model, year, seating_capacity):
        super().__init__(make, model, year)
        self.seating_capacity = seating_capacity
    
    def drive(self):
        print(f"The {self.make} {self.model} is going off-road with a seating capacity of {self.seating_capacity}.")


# Creating car objects
car1 = Car("Toyota", "Corolla", 2021)
car2 = SportsCar("Ferrari", "488 GTB", 2022, 205)
car3 = SUV("Jeep", "Grand Cherokee", 2020, 5)

# Calling methods
car1.drive()
car2.drive()
car3.drive()

import random


class Car:
    def __init__(self, model, color):
        self.fuel = (random.randrange(0,9))
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        if self.fuel >= distance:
            self.trip_distance += distance
            self.fuel -= distance
            print(f"{self.model}: fuel {self.fuel}, passed {distance} km, overall distance: {self.trip_distance} km")
        elif self.fuel > 0:
            actual_distance = self.fuel
            self.trip_distance += actual_distance
            self.fuel = 0
            print(f"{self.model}: no fuel! Passed only {actual_distance} km, overall distance: {self.trip_distance} km")
        else:
            print(f"{self.model}: no fuel!")


car1 = Car("BMW", "Black")
car2 = Car("Mercedes", "White")
car3 = Car("Audi", "Grey")

cars = [car1, car2, car3]

for car in cars:
    print(f"{car.model} {car.color}: fuel = {car.fuel}, distance = {car.trip_distance}")

race_dist = 0
desired_dist = 5

while race_dist < desired_dist:
    cars_with_fuel = [car for car in cars if car.fuel > 0]

    if not cars_with_fuel:
        print("No cars with fuel!")
        break

    for car in cars:
        if car.fuel > 0:
            random_dist = random.randrange(0, 9)
            car.move(random_dist)

            if car.trip_distance > race_dist:
                race_dist = car.trip_distance

            if car.trip_distance >= desired_dist:
                print(f"{car.model} {car.color} won the race! Passed {car.trip_distance} km")
                race_dist = desired_dist
                break
        else:
            print(f"{car.model} {car.color} has no fuel!")

    if race_dist >= desired_dist:
        break


for car in cars:
    print(f"{car.model} {car.color}: fuel = {car.fuel}, distance = {car.trip_distance}")




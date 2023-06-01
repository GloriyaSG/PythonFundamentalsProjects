import re

lines = int(input())
car_mileage_fuel = {}

for line in range(lines):
    cars = input().split("|")
    car = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])
    car_mileage_fuel[car] = {"mileage": mileage, "fuel": fuel}

while True:
    line = input()
    if line == "Stop":
        break
    else:
        command = line.split(" : ")
        car = command[1]
        if command[0] == "Drive":
            distance = int(command[2])
            fuel = int(command[3])
            if car_mileage_fuel[car]["fuel"] < fuel:
                print("Not enough fuel to make that ride")
            else:
                car_mileage_fuel[car]["fuel"] -= fuel
                car_mileage_fuel[car]["mileage"] += distance
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_mileage_fuel[car]["mileage"] >= 100000:
                car_mileage_fuel.pop(car)
                print(f"Time to sell the {car}!")

        elif command[0] == "Refuel":
            fuel = int(command[2])
            if car_mileage_fuel[car]["fuel"] + fuel > 75:
                diff = 75 - car_mileage_fuel[car]["fuel"]
                car_mileage_fuel[car]["fuel"] += diff
                print(f"{car} refueled with {diff} liters")
            else:
                car_mileage_fuel[car]["fuel"] += fuel
                print(f"{car} refueled with {fuel} liters")

        else:
            kilometers = int(command[2])
            car_mileage_fuel[car]["mileage"] -= kilometers
            if car_mileage_fuel[car]["mileage"] < 10000:
                car_mileage_fuel[car]["mileage"] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

for x in car_mileage_fuel:
    print(f"{x} -> Mileage: {car_mileage_fuel[x]['mileage']} kms, Fuel in the tank: {car_mileage_fuel[x]['fuel']} lt.")

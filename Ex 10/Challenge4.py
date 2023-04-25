# Ex 10 Challenge 4
# Paul Takemoto

import vehicles

def main():
    used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0, 4)
    print('Car 1 Make: ', used_car.get_make())
    print('Car 1 Model: ', used_car.get_model())
    print('Car 1 Mileage: ', used_car.get_mileage())
    print('Car 1 Price: ', used_car.get_price())
    print('Car 1 # Doors: ', used_car.get_doors())

    print()

    new_car = vehicles.Automobiles('Honda', 2022, 55000, 85000.0, 4)
    print('Car 2 Make: ', new_car.get_make())
    print('Car 2 Model: ', new_car.get_model())
    print('Car 2 Mileage: ', new_car.get_mileage())
    print('Car 2 Price: ', new_car.get_price())
    print('Car 2 # Doors: ', new_car.get_doors())

main()

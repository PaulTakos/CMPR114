# Ex 10 Challenge 6
# Paul Takemoto

import vehicles2

def main():
    used_car = vehicles2.Automobiles('Audi', '2022', 45000, 80000.0)
    used_car1 = vehicles2.Automobiles('Honda', '2022', 45000, 80000.0)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: $', used_car.get_price())
    print()

    print('Make: ', used_car1.get_make())
    print('Model: ', used_car1.get_model())
    print('Mileage: ', used_car1.get_mileage())
    print('Price: $', used_car1.get_price())
    print()

    truck = vehicles2.Truck('Toyota', 'Tacoma', 40000, 12000.0)
    suv = vehicles2.SUV('Volvo', 'SE', 30000, 18500.0)

    print('The following truck is in inventory: ')
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: $', truck.get_price())
    print()

    print('The following SUV is in inventory: ')
    print('Make: ', suv.get_make())
    print('Model: ', suv.get_model())
    print('Mileage: ', suv.get_mileage())
    print('Price: $', suv.get_price())
    print()

    # New EV object
    ev = vehicles2.EV('Tesla', 'Model S', 35000, 84990.0)

    print('The following EV is in inventory: ')
    print('Make: ', ev.get_make())
    print('Model: ', ev.get_model())
    print('Mileage: ', ev.get_mileage())
    print('Price: $', ev.get_price())

main()

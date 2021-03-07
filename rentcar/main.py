import json

from rentcar.Car import Car
from rentcar.User import Customer

cars = []

base_commands = ("@@@ MENU NAVIGATION @@@ \n" +
                 "/cars - show all available cars \n" +
                 "/my_cars - show all my rented cars \n"
                 "/rent_car - navigate to rent a car \n"
                 "/my_balance - show your current money balance \n")


def get_cars_from_json(var):
    for (k, v) in var.items():
        for car in v:
            cars.append(
                Car(car['make'],
                    car['model'],
                    car['fuel_consumption'],
                    car['reg_number'],
                    car['price_per_hour'],
                    car['price_per_day'],
                    car['price_per_week']))
    pass


def show_all_available_cars():
    for car in cars:
        print(car)
        print("###")
    print("Quantity of cars is:" + str(len(cars)))
    pass


def show_customer_cars(_user):
    if len(_user.rented_car) == 0:
        print("\n" + _user.user_name + " haven't any cars yet!")
    for user_car in _user.rented_car:
        print(user_car.reg_number)
        print(user_car.make)
        print(user_car.model)
        print(user_car.fuel_consumption)
        print("************* \n")


def calculate_price(_car_for_rent, _time_period, _time_quantity):
    if _time_period == "hour":
        _price_per_hour = _car_for_rent.cost.price_per_hour
        _sum = _time_quantity * _price_per_hour
        return _sum
    elif _time_period == "day":
        _price_per_day = _car_for_rent.cost.price_per_day
        _sum = _time_quantity * _price_per_day
        return _sum
    elif _time_period == "week":
        _price_per_week = _car_for_rent.cost.price_per_week
        _sum = _time_quantity * _price_per_week
        return _sum
    else:
        print("Wrong time period")
        return False
    pass


def rent_car():
    _reg_number = input("Enter a registration number ").strip()
    exist = False
    for car_for_rent in cars:
        if car_for_rent.reg_number == _reg_number:
            exist = True
            break
        else:
            exist = False
    if not exist:
        print("Car with " + _reg_number + " doesn't exist in system! Please, enter a correct registration number!")
        rent_car()
    time_period = input("Please, enter time period for rent: "
                        "hour, "
                        "day, "
                        "week").strip()
    time_quantity = int(input("Please, enter how many " + time_period + "s ").strip())

    for car_for_rent in cars:
        if car_for_rent.reg_number == _reg_number:
            calculated_price = calculate_price(car_for_rent, time_period, time_quantity)
            if not calculated_price:
                break
            if len(user.rented_car) >= 2:
                print("You have 30 % discount! ")
                calculated_price = calculated_price - (calculated_price * .30)
            wallet = user.wallet
            if wallet < calculated_price:
                print("Price to pay: " + str(calculated_price))
                print("You don't have money to rent the car for this period! ")
                print("Your balance is: " + str(user.wallet))
                pass
            else:
                print("Price to pay: \n" + str(calculated_price))
                user.wallet = wallet - calculated_price
                cars.remove(car_for_rent)
                user.book_car(car_for_rent)
                print("Your balance is: " + str(user.wallet))
                menu_navigation(input(base_commands).strip())
                pass
    pass


with open('cars.json') as json_file:
    data = json.load(json_file)
    get_cars_from_json(data)

name = input("Welcome to our rent system please enter your name: ").strip()
wallet = int(input("Enter your available money for rent"))
user = Customer(name, wallet)


def menu_navigation(argument):
    if argument == "/cars":
        show_all_available_cars()
    elif argument == "/my_cars":
        show_customer_cars(user)
    elif argument == "/rent_car":
        rent_car()
    elif argument == "/my_balance":
        print("Your balance is: " + str(user.wallet))
    else:
        print("\n Please, enter the correct command !\n", base_commands)
    menu_navigation(input(base_commands).strip())
    pass


navigation = ("Hello, " + name + "\n" +
              base_commands)
command = input(navigation).strip()
menu_navigation(command)

from datetime import datetime


class Car:
    is_booked = False
    # rent_from = datetime.date(datetime.MINYEAR, 1, 1)
    # rent_to = datetime.date(datetime.MINYEAR, 1, 1)

    def __init__(self, make, model, fuel_consumption, reg_number, price_per_hour, price_per_day, price_per_week):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.reg_number = reg_number
        self.cost = Cost(price_per_hour, price_per_day, price_per_week)

    def check_availability(self, requested_rent_from, requested_rent_to):
        if self.rent_from < requested_rent_from < self.rent_to or self.rent_from < requested_rent_to < self.rent_to:
            print("Car " + self.reg_number + " is not available")
            return False
        else:
            return True

    def __str__(self):
        info = "Plate Number: " + self.reg_number + "\nMake: " + self.make + "\nModel: " + self.model + "\nFuel Consumption: " + str(
            self.fuel_consumption) + "\n" + self.cost.__str__()
        return info


class Cost:
    def __init__(self, price_per_hour, price_per_day, price_per_week):
        self.price_per_hour = price_per_hour
        self.price_per_day = price_per_day
        self.price_per_week = price_per_week

    def __str__(self):
        info = "Cost per hour: " + str(self.price_per_hour) + "\nCost per day: " + str(
            self.price_per_day) + "\nCost per week: " + str(self.price_per_week)
        return info


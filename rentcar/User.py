class User:
    def __init__(self, user_name):
        self.user_name = user_name


class Customer(User):
    rented_car = {}

    def __init__(self, user_name, wallet):
        self.wallet = wallet
        super().__init__(user_name)

    def book_car(self, car):
        if car.reg_number not in self.rented_car:
            self.rented_car[car] = car
            # self.rented_car[car.reg_number] = car

        # temp_vehicle = self.rented_car[car.reg_number]
        temp_vehicle = self.rented_car[car]
        temp_vehicle.is_booked = True

        print(car.reg_number+" is booked !")

    def cancel_booking(self, reg_number):
        if reg_number in self.rented_car:
            del self.rented_car[reg_number]

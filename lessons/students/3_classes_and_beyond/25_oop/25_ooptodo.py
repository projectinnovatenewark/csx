"""
Combine all of the concepts of OOP into one problem
"""

class Car:
    """Simple car class"""
    def __init__(self, make, model, year, odometer, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.mpg = mpg
        self.history = {
            "repairs": [],
            "accidents": [],
            "owners": []
        }

    def describe_name(self):
        descriptor = f"This is a {self.year} {self.make} {self.model}"
        print(descriptor)

    def fill_up(self):
        message = f"Now that you filled up, you'll get {self.mpg} miles per gallon!"
        print(message)

    def update_history(self, **kwargs):
        """
        update a car's history including repairs, accidents, and new owners
        pass in any optional arg as either "repair", "accident", or "owner"
        """

        for key, value in kwargs.items():
            history_key = f"{key}s"
            self.history[history_key].append(value)
            history_value_string = ", ".join(self.history[history_key])
            print(f"Here is the vehicle's updated {key} history: {history_value_string}")

    # TODO: Update the "odometer_options" function to accept optional arguments. If an argument of "update" is
    # TODO: passed as the "option", then we should pass an additional argument of "odometer_val".
    # TODO: If the odometer value is less than the current odometer

    def odometer_options(self, option):
        if (option == "update"):

        if (option == "read"):


c1 = Car("Ford", "F150", "2019", 50000, 23)
print(c1.__doc__, "\n")
c1.describe_name()
c1.fill_up()
c1.odometer_options("update", odometer_val=60000)
c1.update_history(repair="new brakes updated", owner="Jake from Statefarm")
c1.update_history(owner="Ricky Bobby")
print("\n")

class ElectricCar(Car):
    """Inherit a car class in a new ElectricCar Class"""
    def __init__(self, make, model, year, odometer, mpg, battery_size, mile_range):
        # we do not want to include mpg in this super function since it doesnt apply to electric vehicles
        super().__init__(make, model, year, odometer, mpg)
        self.mpg = "N/A"
        self.battery_size = battery_size
        self.mile_range = mile_range

    # this is an example of method overriding
    def fill_up(self):
        response = f"You've finished charging your {self.battery_size} battery. You can now travel {self.mile_range} miles"
        print(response)

    # this is a new method specific to the eletric car class
    def describe_range(self):
        response = f"This car has a {self.mile_range} range"
        print(response)

t1 = ElectricCar("Tesla", "Model 3", "2019", 26000, "n/a", "75 kw/h", 250)
# TODO: print out the t1 class's docstring
# this method was inherited from the parent class of Car
t1.describe_name()
# this was also inherited from the parent class
t1.odometer_options("read")
t1.fill_up()
t1.describe_range

# this function represents polymorphism as it can work with different "types" or in our case either
# the ElectricCar class or the Car class
def car_class(obj):
    car_make = "Mercedez"
    print(f"Here is the car_make variable before calling any functions in the car_class func: {car_make}")

    def get_obj_make_nonlocal(obj):
        # TODO: set a nonlocal variable of car_make and update this function's car_make variable
        # TODO: to become the obj's make value.
    
    def get_obj_make_global(obj):
        # TODO: set a global value of car_make and set it's value to "Roll's Royce"

    get_obj_make_nonlocal(obj)
    print(f"Here is the car_make variable within the scope of the car_class function: {car_make}")

    get_obj_make_global(obj)
    print(f"Here is the car_make variable in the car_class function after a global variable assignment: {car_make}")

car_class(t1)
print(f"Here is the car_make variable in the global scope outside of the car_class function: {car_make}")
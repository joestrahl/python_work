class Car():
    """"Representing a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll the mileage back!')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        

        
        

        
my_new_car = Car('ford', 'fusion', 2008)
jordons_car = Car('chevy', 'silverardo', 2006)

my_new_car.update_odometer(234)

jordons_car.odometer_reading = 2348234

print(jordons_car.get_descriptive_name())
jordons_car.read_odometer()

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.increment_odometer(5000)

my_new_car.read_odometer()

class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        self.battery_size = 70
    
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
        
my_tesla = Electric_Car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.read_odometer()
my_tesla.increment_odometer(6546)
my_tesla.read_odometer()


class employee():
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        
    def show_name(self):
        print(self.first.title() + ' ' + self.last.title())
        
    def show_salary(self):
        print('\nYearly Salary: ' + str(self.salary))
        
    def give_raise(self, amount=5000):
        self.salary += amount
        print('\nYour new salary is: ' + str(self.salary))

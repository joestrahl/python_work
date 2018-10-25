from employee_trial import employee
import unittest

class testemployee(unittest.TestCase):
    
    def setUp(self):
        self.person = employee('Joe', 'Strahl', 60000)
        self.salary_1 = 65000
        self.raise_amount = 4000
        self.salary_2 = self.person.salary + self.raise_amount
        
    def test_standard_raise(self):
        self.person.give_raise()
        self.assertEqual(self.person.salary, self.salary_1)
        
    def test_adjustable_raise(self):
        self.person.give_raise(self.raise_amount)
        self.assertEqual(self.person.salary, self.salary_2)

unittest.main()



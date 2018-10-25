class Dog():
	"""A simple attempt to model a dog"""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
		
	def rollover(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")
		
		
my_dog = Dog('Bob', 42), Dog('Bill', 4)

print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is  " + str(my_dog.age) + " years old.")



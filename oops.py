class Animal:
	count = 0

	def __init__(self, count):
		self.count = count

	def add_animal(self):
		Animal.count += 1

	def get_count(self):
		return self.count


class Dog(Animal):
	def __init__(self):
		Animal.__init__(self, 2)

	def say(self):
		Animal.count = 1
		print self.get_count()


a = Dog()
a.say()

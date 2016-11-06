class Animal:
	count = 0

	def add_animal(self):
		Animal.count += 1

	def get_count(self):
		return Animal.count


a = Animal()
b = Animal()

a.add_animal()
print b.get_count(), Animal.count

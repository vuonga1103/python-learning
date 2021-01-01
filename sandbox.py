class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = Dog(name='niko')
felix = Cat(name='felix')

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# <class '__main__.Dog'>
# niko says woof!
# <class '__main__.Cat'>
# felix says meow!


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)  # niko says woof!

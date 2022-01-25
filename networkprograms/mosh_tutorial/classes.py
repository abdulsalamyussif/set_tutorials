class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point = Point(10,20)

point.draw()
print(point.x)

#using a constructor __init__
#
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')
        

yussif = Person('yussif')
yussif.talk()

sakina = Person('Sakina')
sakina.talk()

#inheritance
class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal): 
    def bark(self):
        print('bark')
    

class Cat(Mammal):
    def annoying(self):
        print('be annoying')

dog = Dog()
dog.walk()

cat = Cat()
cat.annoying()


        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking")

    def eat(self):
        print(f"{self.name} is eating")


class Beagle(Dog):
    def __init__(self,name, age, hunter):
        super().__init__(name, age)
        self.hunter = hunter
    def hunt(self):
        print(f"{self.name} is hunting so good")

b1 = Beagle("jessi", 6, True)
b1.bark()
b1.eat()
b1.hunt()
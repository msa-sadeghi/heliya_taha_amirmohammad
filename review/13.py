class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
        
    def walk(self):
        print(f"{self.name} is walking")
  
       
class Student(Person):
    def __init__(self, name, family,class_number):
        super().__init__(name, family)
        self.class_number = class_number
    def study(self):
        print(f"{self.name} is reading")
        

s1 = Student("sara", 'blalal', 12)       
s1.study()       
s1.walk()
        
        

class Teacher(Person):
    def __init__(self, name, family, li):
        super().__init__(name, family)
        self.li = li
    def teaching(self):
        print(f"{self.name} is teaching")
        

s1 = Student("student1", "family1", 12)
t1 = Teacher("teacher1", "family2", "dr")

print(s1.name)
print(s1.family)
print(t1.name)
print(t1.family)

s1.walk()
t1.walk()

t1.teaching()
s1.study()

# class Student:
#     def __init__(self, n, a, g):
#         self.name = n
#         self.age = a
#         self.grade = g
        
#     def display_info(self):
#         print(f"name: {self.name} \nage : {self.age} \n ")
        
# s1 = Student("taha", 12, "A")
# s1.display_info()

# class GraduateStudent(Student):
#     def __init__(self, n, a, g, thesis_title):
#         super().__init__(n, a, g)
#         self.thesis_title = thesis_title
        
#     def display_thesis(self):
#         print(f"name: {self.name} \nage : {self.age} \nthesis is {self.thesis_title} ")
        
# gs1 = GraduateStudent("helia", 10,"A", "AI")
# gs1.display_info()
# gs1.display_thesis()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display_info(self):
#         print(f"{self.name}, {self.age}")
        
# p1 = Person("A", 20)
# p2 = Person("B", 23)
# p1.display_info()
# p2.display_info()


# class Animal:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def walk(self):
#         print(f"{self.name} is walking")
        
# class Cat(Animal):
#     def make_sound(self):
#         print("meo")
# class Dog(Animal):
#     def make_sound(self):
#         print("bark")
        
# c1 = Cat("jessi", 4)
# c1.make_sound()

try:
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    print(x / y)
except ValueError:
    print("value is not valid")
except ZeroDivisionError:
    print("divided by zero")
class Student:
    def __init__(self, name, family, gender, age):
        self.name = name
        self.family = family
        self.gender = gender
        self.age =age
    def study(self):
        print(f"{self.name} is reading")
        
        
s1 = Student("helia", "rashidi", "female", 10)
s2 = Student("taha", "iraji", "male", 12)
s3 = Student("mohammadali", "khezri", "male", 12)
s4 = Student("dariush", "zahedi", "male", 12)

s1.study()
s2.study()
s3.study()
s4.study()
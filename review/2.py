# x = [1,2,3,1]
# print(len(x))
# print(f"count of 1: {x.count(1)}")
# print(x.index(3))
# x.append(100)
# print(x)
# x.pop(2)
# print(x)
# print(1 in x)
# print(1000 in x)
# for number in x:
#     if number == 1:
#         print(True)
#         break
# x.reverse()
# print("x after reversing",x)
# x.sort()
# print("x after ascending sorting", x)
# x.sort(reverse=True)
# print("x after descending sorting", x)
# chars = ["d", "a", "b", "c"]
# chars.sort()
# print(chars)
# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
# print(ord("d"))
# students = ["helia", "taha", "sara","artin", "armin"]
# students.sort()
# print(students)

students = []
for i in range(2):
    student = {}
    name = input("enter a name: ")
    age = int(input("enter an age: "))
    class_number = int(input("enter a class number: "))
    student["name"] = name
    student["age"] = age
    student["class_number"] = class_number
    students.append(student)
    
print(students)
name = input("enter a name: ")
for student in students:
    if student["name"] == name:
        print(student["class_number"])
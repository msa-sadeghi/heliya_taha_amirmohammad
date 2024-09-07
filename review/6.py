# base = int(input("enter a base number: "))
# if base == 0:
#     print("preElementry")
# elif 1 <= base <= 6:
#     print("Elementary")
# elif 7 <= base < 10:
#     print("First highSchool")

# students = []
# for i in range(6):
#     name = input("enter student's name: ")
#     students.append(name)
# print(students)
# print(students[::2])

# python_students = []
# for i in range(5):
#     python_students.append(input("enter a name: "))
    
# print("all students", python_students)
# python_students.append(input("enter a name: "))
# python_students.pop(0)
# print(python_students)

# heights = []
# c = 0
# for i in range(5):
#     h = float(input("enter a height: "))
#     heights.append(h)
#     if 170 <= h <= 180:
#         c += 1
# print(c)
    
# heights = []

# for i in range(5):
#     h = float(input("enter a height: "))
#     if 170 <= h <= 180:
#         heights.append(h)

# print(len(heights))

# scores = []
# for i in range(4):
#     scores.append(float(input(f"score #{i+1}:> ")))
# print(scores)
# for i in range(len(scores)):
#     scores[i] += 2
# print(scores)

x = {
    1 : 'reza',
    2 : 'sara'
}
print(x.get(1))
print(x.get(3))

x[1] = 'mary'
x.update({1: "armin"})
x.update({3: "nikan", 4 : "arsalan"})
print(x)
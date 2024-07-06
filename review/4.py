# def calc_sum(*a):
#     s = 0
#     for number in a:
#         s += number
#     print(s)
    

# calc_sum(12,13,14)
# calc_sum(12,13)
# calc_sum()
# calc_sum(12)

# تابعی بنویسید که میانگین اعداد داده شده را محاسبه و نمایش دهد



# def greet(name="noOne"):
#     return "hello " + name

# print(greet("taha"))
# print(greet())
# s = 0

# def write_to_file(f_name, text):
#     with open(f_name, "a") as f:
#         f.write(text)
        
# write_to_file("1.txt","chera taha nayamad?")

# def read_from_file(f_name):
#     with open(f_name, "r") as f:
#         print(f.read())
        
# read_from_file("1.txt")



# def write_to_file(f_name, text):
#     with open(f_name, "a") as f:
#         f.write(text)
        

# for i in range(3):
#     name = input("enter a name: ")
#     write_to_file("z.txt", name+"\n")

#  پروژه ثبت نام مدرسه
# نام و مشخصات هر دانش آموز را از ورودی دریافت نماید
# برنامه امکان ثبت دانش آموز را در فایل دارد
# برنامه امکان جستجو و نمایش اطلاعات دانش آموز را دارد
# برنامه منو دارد
# hint :  you must use while loop and store all data in a file
# 0  ->    exit
# 1  ->    show all students
# 2  ->    add new student

import json

# name = input("enter your name: ")
# age = input("enter your age: ")
# student = {
#     "name":name,
#     "age": age
# }
# serialized_str = json.dumps(student)
# with open("students.txt", "a") as f:
#     f.write(serialized_str)


# with open("students.txt", "r") as f:
#    text = f.read()
#    obj = json.loads(text)
#    print(obj["name"])

def my_function(r, c):
    if r < 0 or c > 7 or r > 7 or c <0:
        return "error"
    if r % 2 == c % 2:
        return "white"
    return "black"

print(my_function(0,0))
print(my_function(0,3))
print(my_function(1,3))
print(my_function(4,4))
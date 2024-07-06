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



def write_to_file(f_name, text):
    with open(f_name, "a") as f:
        f.write(text)
        

for i in range(3):
    name = input("enter a name: ")
    write_to_file("z.txt", name+"\n")

#  پروژه ثبت نام مدرسه
# نام و مشخصات هر دانش آموز را از ورودی دریافت نماید
# برنامه امکان ثبت دانش آموز را در فایل دارد
# برنامه امکان جستجو و نمایش اطلاعات دانش آموز را دارد
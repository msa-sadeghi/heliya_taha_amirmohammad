# my_dict = {
#     "name" : "dariush", 
# }

# my_dict["name"] = "taha"
# my_dict.update({"name" : "mary"})
# print(my_dict)

my_dict = {
    "python" : 5,
    "js" : 6
}
try:
    name = input("enter the course name:> ")
    my_dict[name] = my_dict.get(name) + 1
except KeyError:
    print("course does'nt exist")
except TypeError:
    print("type")
    

print(my_dict)
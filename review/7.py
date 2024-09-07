x = {"a":"A", "b":"B"}
# try:
#     print(x["c"])
# except:
#     print("hhhhh")
# print(x.get("c"))

x["c"] = "C"
x.update({"d":"D", "e":"E", "a":"a"})
print(x)
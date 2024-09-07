# import time
# item = "mohammad"
# name = "amirmohammad"
# start_time = time.time()
# if item in name:
#     print("found")
# print("test number one",time.time() - start_time)

# start_time = time.time()

# for i in range(len(name)):    
#     if name[i:i+len(item)] == item:
#         print("found")
#         break
# print("test number one", time.time() - start_time)
    
        
students = [
    ("s1", ["armin", 123]),
    ("s2", ["arman", 114]),
    ("s3", ["samin", 104]),    
]    


for num, item in students:
    print(num, item[0], item[1])
students = [
    "armin",
    "arman", 
   "samin"    
]    
for num , item in enumerate(students):
    print(num, item)
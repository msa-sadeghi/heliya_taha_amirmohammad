# name_count = {}
# for i in range(4):
#     name = input("enter a name: ")
#     if name not in name_count:
#         name_count[name] = 1
#     else:
#         name_count[name] += 1
        
# print(name_count)


# sample = [1,2,3,4,1,1,2]
# def find_mode(numbers):
#     number_count = {}
#     mode = None
#     mode_count = 0
#     for n in numbers:
#         if n not in number_count:
#             number_count[n] = 1
#         else:
#             number_count[n] += 1
#         if number_count[n] > mode_count:
#             mode_count = number_count[n]
#             mode = n
#     print(number_count)
#     print(f"mode is {mode} and repeated {mode_count} times")
# find_mode(sample)      
# find_mode([1,2,3,4,66,7,3,55,3,2,1,0,3])      

f = open("test", "w")
print("hello", "friends", sep="*", end=" ", file=f)
print("how are you today?", file=f)
import time
message = "hello friends. how are you today?"
for c in message:
    print(c, end="", flush=True)
    time.sleep(0.2)

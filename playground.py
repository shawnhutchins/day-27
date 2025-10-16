#Add function that takes any number of arguments
def add(*numbers):
    temp = 0
    for num in numbers:
        temp += num
    return temp

print(add(5,7,40,8))
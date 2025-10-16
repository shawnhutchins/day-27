#Add function that takes any number of arguments
def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(add(5,7,40,8))
#Add function that takes any number of arguments
def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(add(5,7,40,8))

#Calculate function that takes any number of named args
def calculate(n, **kwargs):
    for key, value in kwargs.items():
        if key == "add":
            n += value
        elif key == "subtract":
            n -= value
        elif key == "multiply":
            n *= value
        elif key == "divide":
            n /= value
        else:
            print("error")
    print(n)

calculate(3, add=5, multiply=8)
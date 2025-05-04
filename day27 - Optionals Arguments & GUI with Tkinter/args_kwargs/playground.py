
### *ARGS USE EXAMPLE

def add(*args): # args is basically a tuple
    # print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

result = add(5,6,7,8,9,3000)

print(result)

### **KWARGS USE EXAMPLE

def calculate(n, **kwargs): # kwargs is basically a dictionary
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(f"{key} : {value}\n")

    # print(kwargs["add"]) # print a specific value associated with a key in a kwargs

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

### USE OF **kwargs & *args into OO:

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

        # OR
        # self.make = kw.get("make")
        # self.model = kw.get("model") # to avoid KeyError missing kwargs argument if my_car = Car(make="Nissan")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

def Greeting(name):
    print("hello ",name)

# print(Greeting("Ömer"))
# print(Greeting)

sayHello = Greeting

# print(sayHello)
# print(Greeting)

# print(Greeting("Ali"))
# print(sayHello("Ömer"))

# del sayHello
# print(sayHello)
# print(Greeting)
"""
def outer(num1):
    print("outer")
    def inner_increment(num1):
        return num1 + 1
        print("inner")
    num2 = inner_increment(num1)
    print(num1,num2)    


outer(10)         
# inner_increment(10)
"""


def factorial(number):

    if not isinstance(number, int):
        raise TypeError("Number must be integer")

    if not number >= 0:
        raise ValueError("number must be zero or be positive")    

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)        
try:
    print(factorial("2"))
except Exception as ex:
    print(ex)

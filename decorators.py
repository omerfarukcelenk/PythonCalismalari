"""

def my_decorators(func):
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper      

@my_decorators
def sayhello(name):
    print("Hello!!", name)

def sayGreeting():
    print("Greeting")    

sayhello("Ömer")

"""

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,*kwargs)

        finish = time.time()
        print("fonksiyon "+ func.__name__+" "+ str(finish-start)+ " saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):

    print(math.pow(a,b))


@calculate_time
def faktoriel(num):
   
    print(math.factorial(num)) 


usalma(2,3)
faktoriel(4)


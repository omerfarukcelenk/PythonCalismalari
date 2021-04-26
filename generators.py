"""
def cube():
    for i in range(5):
       yield i ** 3 


for i in cube():
    print(i)

"""

list = (i**3 for i in range(5))

print(list)
print(next(list))
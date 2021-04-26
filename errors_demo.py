liste = ["1","2","5a","10b","abc","10","50"]

# Liste elemanları içindeki sayısal değerleri bulunuz .
"""
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue    
"""

# 2 
"""
while True:
    sayi = input("sayı :  ")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print("girdiğiniz sayı : ", result)
    except ValueError:
        print("geçersiz say")
        continue        
"""

# 3

"""
def checkPassword(parola):

    turkce_karakterler = "şçğöüıİ"


    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez")
        else:
            pass

    print("geçerli parola")        

parola = input("parola:  ")

try:
    checkPassword(parola)
except TypeError as error:
    print(error)
"""

# 4 

def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1 , x+1):
        result *= i

    return result    

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = factorial(x)
    except ValueError as error:
        print(error)
        continue
print(y)    
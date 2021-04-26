"""
def usalma(number):
    # two = usalma(2)
    # tree = usalma(3)

    def inner(power):
        return number ** power

    return inner    


two = usalma(2)
tree = usalma(3)    

print(two(3))
print(tree(4))  

"""
"""

def yetki_sorgula(page):
    def inner(role):
        if role == "admin":
            return "{0} rolününün {1} sayfasına ulaşabilir".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)    

    return inner

user1 = yetki_sorgula("Product edit")
print(user1("admin"))
print(user1("user"))

"""

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam       

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i    
        return carpim    

    if islem_adi == "toplama":
        return toplam 
    else:
        return carpma       

toplama = islem("toplama")
print(toplama(1,3,5,7,9))

carpma = islem("carpma")
print(carpma(12,1,5,7)) 
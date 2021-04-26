# try:    
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()



file = open("newfile.txt", "r", encoding= "utf-8")

# for döngüsü ile
"""
for i in file:
    print(i, end="")
"""

# ***************read() fonksiyonu ile
"""
content1 = file.read()

print("içerik 1")
print(content1)


file = open("newfile.txt", "r", encoding= "utf-8")

content2 = file.read()

print("içerik 2")
print(content2)
file.close()
"""
"""
content1 = file.read(5)
content2 = file.read(2)
content3 = file.read(3)

print(content1)
print(content2)
print(content3)

file.close()
"""

# ***************readline() fonksiyonu ile


print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")

file.close()
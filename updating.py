# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")   


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#     SAYFA SONUNDA GÜNCELLEME

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nselo celo")


#     SAYFA BASINDA GÜNCELLEME
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "MELİS GÖK \n" + content
    file.seek(0)
    file.write(content)
    print(content)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())

"""
#       SAYFA ORTASINDA GÜNCELLEME

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Hediye ET \n")
    file.seek(0)
    for i in list:
        file.write(i)
    
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())

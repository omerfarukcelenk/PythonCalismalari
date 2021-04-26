# with dosyanın otomatik kapanmasını sağlıyor    

with open("newfile.txt", "r", encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)


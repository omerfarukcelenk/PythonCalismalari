import os
import datetime

result = dir(os)
result = os.name
# os.chdir("C:\\")
# os.chdir("../..")
# result = os.getcwd()

#   klosör oluşturma

# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")

# listeleme

# result = os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

# result = os.stat("date.py") 
# result = result.st_size/1024 
# result = datetime.datetime.fromtimestamp(result.st_ctime)      # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)      # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)      # değiştirilme tarihi

# os.system("notepad.exe")

# os.rename("newdirectory","DENEMEklasörü")
# os.rmdir("silmelik")
# os.removedirs("DENEMEklasörü/yeniklasör")


# path


result = os.path.abspath("_os.py")
result = os.path.dirname("D:/Python/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("_os.py")
result = os.path.isdir("D:/Python/_os.py")
result = os.path.isfile("D:/Python/_os.py")
result = os.path.join("C://","deneme","deneme1")
result = os.path.split("C://deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]







print(result)
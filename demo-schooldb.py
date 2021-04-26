import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "schooldb"
)



class Student:
    connection = connection
    mycursor = connection.cursor()


    def __init__(self, studentnumber,name,surname,birthdata,gander):
        self.studentnumber = studentnumber
        self.name   = name
        self.surname = surname
        self.birthdata = birthdata
        self.gander = gander    
    
    def saveStudent(self):
        sql = "INSERT INTO students (studentnumber,name,surname,birthdata,gander"
        values = (self.studentnumber,self.name,self.surname,self.birthdata,self.gander)




ogrenciler = [
    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
]

mycursor.executemany(sql, ogrenciler)

try:
    connection.commit()
    print(f"{mycursor.rowcount} tane kayıt eklendi.")
except mysql.connector.Error as err:
    print("hata : ", err) 
finally:
    connection.close()



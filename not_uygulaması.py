def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3 

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >=85 and ortalama < 90:
        harf = "BA"
    elif ortalama >=80 and ortalama < 85:
        harf = "BB"
    elif ortalama >=75 and ortalama < 80:
        harf = "BC"        
    elif ortalama >=70 and ortalama < 75:
        harf = "CC"
    elif ortalama >=65 and ortalama < 70:
        harf = "DC"
    elif ortalama >=60 and ortalama < 65:
        harf = "DD"    
    elif ortalama >=50 and ortalama < 60:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"          


def ortalamarı_oku():
    with open("sinav_notları.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))





def not_gir():
    ad = input("Öğrenci adı: ")
    soyadı = input("Öğrenci soyadı: ")
    not1 = input("1.notu: ")
    not2 = input("2.notu: ")
    not3 = input("3.notu: ")


    with open("sinav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad+ " " + soyadı + ":" + not1 + "," + not2 + "," + not3 + "\n")


def notları_kayıt_et():
    with open("sinav_notları.txt","r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:

            for i in liste:
                file2.write(i)



while True:
    islem = input("1- Notları oku \n2- Not Gir \n3- Notları Kayıt Et \n4- Çıkış\n")

    if islem == "1":
        ortalamarı_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notları_kayıt_et()
    else:
        break

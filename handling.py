# Error Handling => Hata yönetimi
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz !!!", ex)    
    else:
        break   
    finally:
        print("try expect sonlandı.") 
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır

# Kulanımı : open(dosya_adı,dosya_erişme_modu) 

# Dosya_erişme_modu => Dosyayı hangi amaçla açtığımızı belirtir.

# "w" (write) yazma modu . Dosyayı konumda oluşturur.

# file = open("newfile.txt","w")
# file.close()

file = open("C:/users/casper/desktop","w")
print(file)

# "a" (append) ekleme modu . Dosya konumda yoksa oluşturur.

# "x" (create) oluşturma . Dosya zaten varsa hata verir.

# "r" (read) okuma . varsayılan dosya kunumda yoksa hata verir.
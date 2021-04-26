import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_Doviz = input("Bozulan dövüz türü : ")
alınan_doviz = input("Alınan dövüz türü : ")
miktar = int(input(f"Ne kadar {bozulan_Doviz} bozdurmak istiyorsunuz ? : "))

result = requests.get(api_url+bozulan_Doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_Doviz, result["rates"][alınan_doviz],alınan_doviz))
print("{0} {1} = {2} {3} ".format(miktar, bozulan_Doviz, miktar * result["rates"][alınan_doviz], alınan_doviz ))

print(result)
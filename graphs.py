import matplotlib.pyplot as plt
"""
# Stack Plot

yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [6,13,19,15,8]
oyuncu3 = [18,10,12,17,6]


plt.plot([],[],color = "y",label="oyuncu 1")
plt.plot([],[],color = "r",label="oyuncu 2")
plt.plot([],[],color = "b",label="oyuncu 3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan göller")
plt.xlabel("yıl")
plt.ylabel("golsayısı")

plt.legend()
plt.show()

"""

"""
# Pie Grafiği

goal_types = "Penaltı","Kaleye Atılan Şut","Serbest Vuruş"

goals = [12,35,7]
colors = ["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct ="%1.1f%%" )
plt.legend()
plt.show()
"""
"""

# Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="AUDİ",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")

plt.show()

"""
"""
# Histogram Grafiği

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_grupları = [0,10,20,30,40,50,60,70,80,90,100]


plt.hist(yaslar,yas_grupları,histtype="bar",rwidth=0.8)
plt.xlabel("Yaş Gurupşarı")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")

plt.show()

""" 
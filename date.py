from datetime import datetime
from datetime import timedelta



"""
from datetime import date
from datetime import time
import datetime
"""

simdi = datetime.now()

simdi = datetime.today()
# result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")
result = datetime.strftime(simdi,"%X")
result = datetime.strftime(simdi,"%D")
result = datetime.strftime(simdi,"%A")
result = datetime.strftime(simdi,"%B")
result = datetime.strftime(simdi,"%Y %B %A")


t = "15 april 2020 hour 12:12:30"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S") 
result = result.year

birthday = datetime(2000, 12, 12, 8,30,00)

result = datetime.timestamp(birthday)   # saniye
result = datetime.fromtimestamp(result) # saniyeyi datetime a çevirir
result = datetime.fromtimestamp(0)

result = simdi - result # timedelta objesi

# result = result.days 
# result = result.seconds
# result = result.microseconds

result = simdi + timedelta(days= 10)
result = simdi + timedelta(days= 730)
result = birthday - timedelta(days= 100)




print(result)
print(birthday)

"""
gun, ay, yıl = t.split()
t = "21 Nisan 2019"
print(gun)
print(ay)
print(yıl)

"""




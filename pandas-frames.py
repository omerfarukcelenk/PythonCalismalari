import pandas as pd

list = [["AHMET",50],["ALİ",60],["YAĞMUR",70],["ÇINAR",80]]
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
dict_list = [
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Çınar","Grade":80}
    ]
# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(list ,columns = ["Name","Grade"], index = [1,2,3,4], dtype = float)
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["2453","4786","4237","2379"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index = ["2453","4786","4237","2379"])



print(df)






# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)

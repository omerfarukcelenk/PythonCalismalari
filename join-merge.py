import pandas as pd

# customers = {
#     "CustomerId": [1,2,3,4],
#     "FirsName": ["Ahmet","Ali","Ömer","Mehmet"],
#     "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
# }

# orders = {
#     "OrderId": [10,11,12,13],
#     "CustomerId": [1,2,5,7],
#     "OrderDate": ["2011-07-04","2012-10-18","2013-04-24","2015-03-30"]
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirsName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers ,df_orders, how = "inner")
# result = pd.merge(df_customers ,df_orders, how = "left")
# result = pd.merge(df_customers ,df_orders, how = "right")




customersA = {
    "CustomerId": [1,2,3,4],
    "FirsName": ["Ahmet","Ali","Ömer","Mehmet"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
}



customersB = {
    "CustomerId": [4,5,6,7],
    "FirsName": ["Kerim","Muzaffer","Aşkın","Selim"],
    "LastName": ["Bal","Velan","Toprak","Efendi"],
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirsName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirsName","LastName"])

result = pd.concat([df_customersA,df_customersB])
result = pd.concat([df_customersA,df_customersB],axis=1)



print(result)
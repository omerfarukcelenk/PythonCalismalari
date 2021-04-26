import json

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isloggedin = False
        self.currentuser = {}

        # load use1rs from .json file
        self.loadUsers()

    def loadUsers(self):
        pass    

    def register(self,user: User):
        self.users.append(user)
        self.savetofile()
        print("kullanıcı oluşturuldu")

        
    def login(self):
        pass
    def savetofile(self):
        list = []
        
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json","w") as file:
            json.dumb(list, file)



Repository = UserRepository()






while True:
    print("menü".center(50,"*"))
    secim = input("1- register \n2- login\n3- logout\n4- identity\n5- exit\n seçiminiz : ")    
    if secim == "5":    
        break 
    else: 
        if secim == "1":
            #register
            username = input("Username : ")
            password = input("password : ")
            email = input("email : ")

            user = User(username=username, password=password,email=email)
            Repository.register(user)
            print(Repository.users)
        elif secim == "2":
            #login
            pass
        elif secim == "3":
            #logout
            pass
        elif secim == "4":
            #identity
            pass
        else: 
            print("Yanlış Seçim !?!?!")
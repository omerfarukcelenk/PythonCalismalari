import requests

class Github:
    def __init__(self):
        self.api_url = "https://github.com/"

    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+ username)    
        return response.json()

github = Github()


while True:
    secim = input("1 - find user\n2 - get repositories\n3 - Creat repositories\n4 - Exit\nSeçim :  ")

    if secim == 4:
        break
    else:
        if secim == 1:
            username = input("username : ")
            result = github.getUser(username)
            print(result)
        elif secim == 2:
            pass    
        elif secim == 3:
            pass
        else:
            pass     
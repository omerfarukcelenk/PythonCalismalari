Mylist = [1,2,3]
# MyString = "my string"

# print(len(Mylist))
# print(len(MyString))
# print(type(Mylist))
# print(type(MyString))


class movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu !!")

    def __str__(self):
        return f"{self.title} by {self.director} "   
    def __len__(self):
        return self.duration

    def __del__(self):
        print("movie silindi!!") 




m = movie("film adı", "yönetmen adı", 120)
print(str(Mylist))
print(str(m))
print(len(Mylist))
print(len(m))

# print(len(m))
# print(type(m))

del m 

print(m)
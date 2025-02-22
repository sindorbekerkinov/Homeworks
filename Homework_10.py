# class User:
#     """Malumotnoma"""
#     def __init__(self, Ism, Familya, Email, Age):
#         self.ism = Ism
#         self.familya = Familya
#         self.email = Email
#         self.age = Age
#
#
#     def get_name(self):
#         self.ism = input("Imingizni kiriting: ")
#         return self.ism
#     def get_lastname(self):
#         self.familya = input("Familyaningizni kiriting: ")
#         return self.familya
#     def get_email(self):
#         self.email  = input("Email kiriting: ")
#         return self.email
#     def get_age(self):
#         self.age = int(input("Yoshingizni kiriting: "))
#         return self.age
#     def get_info(self):
#         print(f"Ism {self.ism} Familya {self.familya} Email {self.email} Yosh {self.age}")
#
# user1 = User (" ", " ", " ",0 )
# user1.get_name()
# user1.get_lastname()
# user1.get_email()
# user1.get_age()
# user1.get_info()


class User:
    def __init__(self, ism, familya, tyil, email):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.email = email

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.ism

    def get_tyil(self):
        return self.tyil

    def get_email(self):
        return self.email

user_1 = User ("Sindorbek","Erkinov",2006,"sindorbekerkinov@gamil.com")
user_2 = User ("Ali", "Valiyev", 2000, "alivali@gmail.com")
user_3 = User ("Bekzod", "Matrasulov", 2003,"bekzodmatrasulov@gmail.com")
print(user_3.get_tyil())
print(user_1.get_email())
print(user_2.get_lastname())
print(user_3.get_name())
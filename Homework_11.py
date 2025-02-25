# class Texnika:
#     """Texnika haqida malumot"""
#     def __init__(self,brand,model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#     def info(self):
#             print(f"Texnikani brendi: {self.brand}, Modeli: {self.model}, Turi: {self.type}")
#
# class Notebooks(Texnika):
#     def __init__(self,brand,model, type,video_card, ram ,display):
#         super().__init__(brand,model, type)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#     def more_info(self):
#         print(f"Texnikani brendi: {self.brand}, Modeli: {self.model}, Turi: {self.type}\n"
#               f"Video kartasi: {self.video_card}, RAM: {self.ram}, Ekran: {self.display}")
#
# class Televisions(Texnika):
#     def __init__(self,brand,model,type,size,display):
#         super().__init__(brand,model,type)
#         self.size = size
#         self.display = display
#     def more_info(self):
#         print(f"Texnikani brendi: {self.brand}, Modeli: {self.model}, Turi: {self.type}\n"
#               f"O'chami: {self.size}, Ekrani: {self.display}")
# class Smartphones(Texnika):
#     def __init__(self,brand,model, type,size, sim_count):
#         super().__init__(brand,model, type)
#         self.size = size
#         self.sim_count = sim_count
#     def more_info(self):
#         print(f"Texnikani brendi: {self.brand}, Modeli: {self.model}, Turi: {self.type}\n"
#               f"O'lchami: {self.size}, Sim kartasi:{self.sim_count}")
#
#
# Telefon = Smartphones("Samsung","Oxirgi", "S25 Ultra", "3120x1440", "2")
# Telefon.more_info()
# texnika = Texnika("Samsung", "So'ngi","maishiy texnika")
# # texnika.info()
#
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#
# class Transport:
#     def __int__(self,brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type} ")
# class ElektroCars(Transport):
#     def __init__(self,brand, model, type,battery_life,chargin_time):
#         super().__init__(brand, model, type)
#         self.battery_life = battery_life
#         self.chargin_time = chargin_time
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}\n"
#               f"Batariyaning chidamliligi: {self.battery_life}, Zaryadlash muddati: {self.chargin_time}")
# class SportCars(Transport):
#     def __init__(self,brand, model, type,motor, color):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}\n"
#               f"Motor: {self.motor}, Rangi: {self.color}")
# class Truck(Transport):
#     def __init__(self,brand, model, type,height, long,wieght):
#         super().__init__(brand, model, type,)
#         self.height = height
#         self.long = long
#         self.weight = wieght
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}\n"
#               f"Balandligi: {self.height}, Uzunligi: {self.long}, Vazni: {self.weight}")
#
#
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
class University:
    def __init__(self,university):
        self.university = university
    def info(self):
        print(f"Universitet: {self.university}")

class Staff(University):
    def __init__(self,university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def more_info(self):
        print(f"Universitet: {self.university}, Ism: {self.first_name}, Familya:{self.last_name}\n"
              f"Yosh: {self.age}")
class Student(Staff):
    def __init__(self,university, first_name, last_name, age,group):     
        super().__init__(university, first_name, last_name, age)
        self.group = group

    def more_info(self):
        print(f"Universitet: {self.university}, Ism: {self.first_name}, Familya:{self.last_name}\n"
              f"Yosh: {self.age}, Guruh: {self.group}")
class Teacher(Staff):
    def __init__(self,university, first_name, last_name,position, subject):
        super().__init__(university, first_name, last_name)
        self.position = position
        self.subject = subject
    def more_info(self):
        print(f"Universitet: {self.university}, Ism: {self.first_name}, Familya:{self.last_name}\n"
              f"Darajasi: {self.position}, Fani: {self.subject}")
class OtherStaff(Staff):
    def __init__(self,university, first_name, last_name,position,):
        super().__init__(university, first_name, last_name)
        self.position = position
    def more_info(self):
        print(f"Universitet: {self.university}, Ism: {self.first_name}, Familya:{self.last_name}\n"
              f"Darajasi: {self.position}")

class Object(University):
    def __init__(self, university,name):
        super().__init__(university)
        self.name = name
    def object_info(self):
        print(f"Universitet: {self.university}, Name: {self.name}")
class Computer(Object):
    def __init__(self,university,name, soni, tizimi,holati):
        super().__init__(university,name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati
    def object_more_info(self):
        print(f"Universitet: {self.university}, Name: {self.name}, Soni: {self.soni}\n"
              f"Tizimi: {self.tizimi}, Holati: {self.holati}")
class Mabel(Object):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.turi = turi
        self.holati = holati
    def object_more_info(self):
        print(f"Universitet: {self.university}, Name: {self.name}, Soni: {self.soni}\n"
              f"Turi: {self.turi}, Holati: {self.holati}")

Tatu = Student("UBTUIT", "Javohir", "Bekturdiyev", 19, "961-24")
Tatu.more_info()
#

# davlatlar_poytaxtlar = {
#     "AQSH":"Washington",
#     "Italya":"Rim",
#     "Malayziya":"Kuala-Lumbur",
#     "O'zbekiston":"Toshkent",
#     "Qirg'izton":"Bishkek",
#     "Qozoqiston":"Nursulton",
#     "Rossiya":"Moskva",
#     "Singapur":"Sungapur",
#     "Tojikiston":"Dushanbe"
# }
#
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar_poytaxtlar.keys()):
#     print(davlat)
# print("\nDavlatlarning poytaxtlari:")
# for poytaxt in sorted(davlatlar_poytaxtlar.values()):
#     print(poytaxt)

# davlat = input("\nQaysi davlatning poytaxtini bilishni istaysiz?: ").upper()
# if davlat in davlatlar_poytaxtlar:
#     print(f"{davlat}ning poytaxti {davlatlar_poytaxtlar[davlat]} shahri.")
# else:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q.")


menyu = {
    "osh": 20000,
    "sho'rva": 15000,
    "norin": 18000,
    "lag'mon": 22000,
    "somsa": 8000,
    "shashlik": 12000,
    "manti": 10000,
    "non": 4000,
    "salat": 7000,
    "kabob": 25000
}
print("3 ta taom buyurtma bering.")
buyurtmalar = []

for a in range(3):
    taom = input(f"{a+1}-taom: ").lower()
    buyurtmalar.append(taom)

print("\nBuyurtmalar natijasi:")

for taom in buyurtmalar:
    if taom in menyu:
        print(f"{taom.capitalize()} {menyu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q.")




















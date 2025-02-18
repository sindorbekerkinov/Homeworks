# N=1
# def str_counter(strs):
#     natija = {}
#     for s in strs:
#         uzunlik = len(s)
#         natija[uzunlik] = s
#     return natija
# print(str_counter(["shaftoli", "olma", "nok"]))
# str_counter(["shaftoli", "olma", "nok"])

# n=2
# def merge_list(list1, list2):
#     if len(list1) != len(list2):
#         print("listlar teng emas!")
#     return dict(zip(list1, list2))
# list1 = [1,2,3]
# list2 = ["a", 'b','c']
# print(merge_list(list1, list2))
# merge_list(list1, list2)

# n=3
# contacts = {
#     "Nodir": "+998918602711",
#     "Laziz": "+998908002534"
# }
#
#
# def show_menu():
#     print("\nTelefon Kontaktlar Ro'yxati:")
#     print("1. Kontakt qo'shish")
#     print("2. Kontakt yangilash")
#     print("3. Kontakt o'chirish")
#     print("4. Kontakt qidirish")
#     print("5. Barcha kontaktlarni ko'rish")
#     print("6. Chiqish")
#
#
# def add_contact():
#     name = input("Ism kiriting: ")
#     phone = input("Telefon raqamini kiriting: ")
#     if name in contacts:
#         print(f"{name} allaqachon mavjud!")
#     else:
#         contacts[name] = phone
#         print(f"{name} qo'shildi.")
#
#
# def update_contact():
#     name = input("Yangilash uchun ism kiriting: ")
#     if name in contacts:
#         phone = input("Yangi telefon raqamini kiriting: ")
#         contacts[name] = phone
#         print(f"{name} yangilandi.")
#     else:
#         print(f"{name} mavjud emas!")
#
#
# def delete_contact():
#     name = input("O'chirish uchun ism kiriting: ")
#     if name in contacts:
#         del contacts[name]
#         print(f"{name} o'chirildi.")
#     else:
#         print(f"{name} mavjud emas!")
#
#
# def search_contact():
#     name = input("Qidirish uchun ism kiriting: ")
#     if name in contacts:
#         print(f"{name}: {contacts[name]}")
#     else:
#         print(f"{name} topilmadi!")
#
#
# def view_all_contacts():
#     if contacts:
#         print("\nBarcha kontaktlar:")
#         for name, phone in contacts.items():
#             print(f"{name}: {phone}")
#     else:
#         print("Kontaktlar ro'yxati bo'sh!")
#
#
# def main():
#     while True:
#         show_menu()
#         choice = input("\nTanlovingizni kiriting (1-6): ")
#
#         if choice == '1':
#             add_contact()
#         elif choice == '2':
#             update_contact()
#         elif choice == '3':
#             delete_contact()
#         elif choice == '4':
#             search_contact()
#         elif choice == '5':
#             view_all_contacts()
#         elif choice == '6':
#             print("Dastur yakunlandi.")
#             break
#         else:
#             print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
#
#
# if __name__ == "__main__":
#     main()
#
# # n=4
# def counter_dict(nums):
#     count_dict = {}
#     for num in nums:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#     return count_dict
#
# print(counter_dict([2, 1, 1, 1]))
# print(counter_dict([4, 4, 4, 2, 2, 3]))
# print(counter_dict([5, 5, 5, 5, 5]))
# print(counter_dict([]))

# n=5
# def max_ball_students(talabalar):
#     saralangan = sorted(talabalar.items(), key=lambda x: x[1], reverse=True)
#     eng_yaxshi_ikkita = dict(saralangan[:2])
#     return eng_yaxshi_ikkita
#
#
# print(max_ball_students({"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}))









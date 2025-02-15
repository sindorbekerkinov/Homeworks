# def daraja(a='',b=''):
#     a = int(input("Son kiriting: "))
#     b = int(input("Nechinchi darajaga ko'tarmoqchisiz: "))
#     c= a**b
#     print(c)
#     return daraja()
# daraja()



# def daraja(a,b):
#     c= a**b
#     return c
# a = int(input("Son kiriting: "))
# b = int(input("Nechinchi darajaga ko'tarmoqchisiz: "))
# print(daraja(a,b))
# daraja()



# #N=6
# def daraja(a='',b='',c='',d=''):
#     a = int(input("Son kiriting: "))
#     b = int(input("Nechinchi darajaga ko'tarmoqchisiz: "))
#     c = int(input("Son kiriting: "))
#     d = int(input("Nechinchi darajaga ko'tarmoqchisiz: "))
#     w =a**b
#     s =c**d
#     print(w, s)
# daraja()

# N=7
# def digit_count_and_sum(word=''):
#     word = input("So'zni kiriting:")
#     count = 0
#     sum = 0
#     for i in word:
#         if i.isdigit():
#             count += 1
#             sum += int(i)
#     print(f"Chiqarilgan sonlar soni: {count}\n"
#           f"Chiqarilgan sonlar to'plami: {sum}")
# digit_count_and_sum()

# N=8
# def add_right(a='', b=''):
#     a = int(input("Son kiriting: "))
#     b = int(input("Son kiriting: "))
#     print(f"{a}{b}")
# add_right()

# N=9
# def add_left(a='',b=''):
#     a = int(input("Son kiriting: "))
#     b = int(input("Son kiriting: "))
#     print(f"{b}{a}")
# add_left()

# N=10
# def work_with_lists(a=''):
#     a= [7,4,5,6,2,10]
#     b = min(a)
#     c =[]
#     for n in a:
#         c.append(n*b)
#     print(c)
# work_with_lists()

# # n=11
# def big_sales(sales=''):
#     sales={
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
#     }
#     a= max(sales.values())
#     print(a)
# big_sales()


# # n=12
# def min_max(numbers,max_num,min_num):
#     maximum=max(numbers)
#     minimum=min(numbers)
#
#     if maximum==max_num:
#         print(f"{max_num} son ro'yxatdagi eng katta son")
#     else:
#         print(f"{max_num} son ro'yxatdagi eng katta son emas")
#
#     if minimum==min_num:
#         print(f"{min_num} son ro'yxatdagi eng kichik son")
#     else:
#         print(f"{min_num} son ro'yxatdagi eng kichik son emas")
# numbers=[1,-9,41,36,0,9,0,13]
# katta=41
# kichik=0
# min_max(numbers,katta,kichik)
#
# # n=13
# def expensiveProduct(products):
#     max_price = max(product["price"] for product in products)
#     return max(product["name"] for product in products if product["price"] == max_price)
#
# products = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1100
#     },
# ]
#
# print(expensiveProduct(products))






























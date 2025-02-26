with open('pi_million_digits.txt') as file:
    pi = file.read()

def check_num():
    t_yil = input("Tug'ilgan sanangiz: ")
    ishora = True
    while ishora:
        if not t_yil in pi:
            ishora = False
            print("Sizning tug'ilgan sanangiz bu raqamlar ichida yo'q! ")

        else:
            print("Sizning tug'ilgan kuniningiz bor! ")

            import pickle
            with open("info.dat","wb") as fayl:
                pickle.dump(t_yil,fayl)
            break
check_num()

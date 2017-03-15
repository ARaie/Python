from random import randint

check = randint(0, 9)
print(check)
def loto(): #iseenese poole pöördumine on rekursioon
    number = input("Sisesta number 0-9: ")
    if number.isdigit():
        number = int(number)
        if number < check:
            print("Väiksem")
            loto()
        elif number > check:
            print("Suurem")
            loto()
        else:
            print("Võrdsed")
    else:
        print("See pole ju number!")
loto()
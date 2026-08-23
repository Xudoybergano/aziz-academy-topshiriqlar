menu = int(input())
score = int(input())

if menu == 1:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
elif menu == 2:
        if score >= 60:
            print("O'tdi")
        else:
            print("Yiqildi")
else:
    print("Notogri tanlov")
          
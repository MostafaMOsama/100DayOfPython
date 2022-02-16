# Tip calucate App
import time
from About import info


def Tipcalculator():
    print(info)
    while True:
        bill = float(input("Enter Bill Amount ? "))
        tip = int(input("How much tip do you want to pay ? "))
        people = int(input("how many pepel : "))
        tipPercent = tip / 100
        total_tip_amount = bill * tipPercent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 0)

        print(f"ever one must pay {final_amount} $")

        again = str(
            input("if u need close App Pres (Y) Contain Press (N) : ").upper())

        if again == "Y":
            for count in range(3):
                print("App closing Plesa Wait..... ")
                # Prints the current time with a five second difference
                time.sleep(2)

            break
        else:
            continue


Tipcalculator()

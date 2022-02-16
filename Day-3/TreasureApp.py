# project in if statament and flow
import time
import Main
from about import info


def TreasureGame():
    print(info)
    while True:
        choice1 = input(
            "'You are at a crossroad. Where do you want to go? Type (left) or (right) : ").lower()
        if choice1 == "left":
            choice2 = input(
                "You have come to a lake. There is an island in the middle of the lake. Type (Wait ) to wait for a boat. Type (Swim) to swim across. : ")
            if choice2 == "wait":
                choice3 = input(
                    "You arrive at the island unharmed. There is a house with 3 doors. (One red), (one yellow) and one (blue). Which colour do you choose ?  ")
                if choice3 == "red":
                    print("It's a room full of fire. Game Over.")
                elif choice3 == "yellow":
                    print("You found the treasure! You Win !")
                elif choice3 == "blue":
                    print("You enter a room of beasts. Game Over")
                else:
                    print("You chose a door that doesn't exist . Game Over")
            else:
                print("You get attacked by an angery trout . Game Over ")
        else:
            print("you Fell into Hole .Game Over ")
        again = str(
            input("if u need close App Pres (Y) Contain Press (N) : ").upper())

        if again == "Y":
            for count in range(3):
                print(f"App closing Plesa Wait..... {count + 1}")
                # Prints the current time with a five second difference
                time.sleep(3)

            break
        else:
            continue


TreasureGame()

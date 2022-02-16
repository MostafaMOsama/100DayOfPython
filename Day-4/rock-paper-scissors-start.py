import random
import time
from About import info


def play():
    print(info)
    while True:
        rock = '''
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
            '''

        paper = '''
                _______
            ---'   ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            '''

        scissors = '''
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
            '''

        print(rock, paper, scissors)
        game = ["rocket", "paper", "scissors"]
        randomGame = random.choice(game)
        player = str(
            input("Choice one of (Rocket) , (Paper) , (Scissors) : ").lower())
        if player == "rocket" and randomGame == "scissors" or player == "paper" and randomGame == "rocket" or player == "scissors" and randomGame == "paper":
            print(
                f"You Choice ({player}) and Computer Choice ({randomGame}) You Win (^-^)")
        elif player == randomGame:
            print(
                f"You Choice ({player}) and Computer Choice ({randomGame}) It's a Tie (.....)")

        else:
            print(
                f"Computer Choice  ({randomGame}) and you Choice ({player}) You Lose !!")
        again = input(
            "if u need close App Pres (Y) Contain Press (N) : ").upper()
        if again == "Y":
            for count in range(3):
                if count == 0:
                    print("Cye you again .")
                    time.sleep(1)
                if count == 1:
                    print("Cye you again ..")
                    time.sleep(1)
                if count == 2:
                    print("Exit (^_^)")
                    time.sleep(1)
            break
        else:
            for count in range(5):
                if count == 0:
                    print("Loading.")
                    time.sleep(1)
                if count == 1:
                    print("Loading..")
                    time.sleep(1)
                if count == 1:
                    print("Loading...")
                    time.sleep(1)
                if count == 1:
                    print("Loading....")
                    time.sleep(1)
                if count == 1:
                    print("Let's Play Again <3 (^-^)")
                    time.sleep(1)


play()

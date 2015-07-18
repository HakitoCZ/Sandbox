#!/usr/bin/python3

from random import randint

roll_total = 0
game = 1
player_turn = 1
dealers_total = 0

print("Throw 21 with two D6.")
print("Type 'roll' to start and 'stop' to end your turn.")
while game == 1:
    try:
        user_input = str(input("> "))
    except KeyboardInterrupt:
        print("\nQuitting..")
        break
    except EOFError:
        print("Quitting..")
        break

    if user_input == "about":
        print("This game was made within a period of three days. Hope you'll\
enjoy it.")
    if user_input == "roll":
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        roll = d1 + d2
        roll_total += roll
        print("You threw", d1, "and", d2)
        print("Total:", roll_total)
        if roll_total > 21:
            print("Lost")
            game = 0
        elif roll_total == 21:
            print("WIN!!")
            game = 0
    
    elif user_input == "stop":
        player_turn = 0

    else:
        print("Try again")

    while player_turn == 0:
        print("Dealer's turn, press Enter.")

        try:
            user_input = str(input("> "))
        except KeyboardInterrupt:
            print("\nQuitting..")
            break
        except EOFError:
            print("Quitting..")
            break

        d1 = randint(1, 6)
        d2 = randint(1, 6)
        dealers_roll = d1 + d2
        dealers_total += dealers_roll
        print("Thrown", d1, "and", d2)
        print("Total:", dealers_total)
        if dealers_total > 21:
            print("You Win!")
            game = 0
            break
        elif dealers_total == 21:
            prin("Dealer Wins")
            game = 0
            break
        if dealers_total in range(15, 21):
            if roll_total > dealers_total:
                print("You Win! with", roll_total)
                game = 0
                break
            elif roll_total == dealers_total:
                print("Draw")
                game = 0
                break
            else:
                print("Dealer wins.")
                game = 0
                break


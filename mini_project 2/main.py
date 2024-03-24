import random

command = input("You need instructions type? (yes / no)")

if command.lower() == "no":
    print("LET'S START THE GAME")
elif command.lower() == "yes":
    print("1.The player should roll two dice.\n2. If the sum of both of them is 7 or 11 the player wins. If the sum "
          "is 2, 3 or 12 (craps) the casino wins. \n3. If during the first roll the sum is 4, 5, 6, 8, 9 or 10, "
          "that number becomes the “goal” number. \n4. To win, the player should roll the dice till they roll the goal "
          "number again. If the player rolls a 7 before rolling the goal number, they lose. \n============")
else:
    command = input("Press enter to to START game")


def dice_number():
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)

    return dice1, dice2


def dice_result(dices):
    dice1, dice2 = dices
    print("The sum of die is {} + {} = {}".format(dice1, dice2, sum(dices)))


def start_game():
    next_step = True
    value = dice_number()
    dice_result(value)
    sum_of_dices = sum(value)

    if sum_of_dices in (7, 11):
        result = "You won"
        next_step = False
    elif sum_of_dices in (2, 3, 12):
        next_step = False
        result = "You lost! \nTry again next time"
    else:
        next_step = True
        current = sum_of_dices
        print("Now your goal number is", current)

    while next_step == True:
        value = dice_number()
        dice_result(value)
        sum_of_dices = sum(value)

        if sum_of_dices == current:
            result = "You won"
            next_step = False
        elif sum_of_dices == 7:
            result = "You lost! \n Try again next time"
            next_step = False

    print("============")
    if result == "You won":
        print("You won")
    else:
        print("You lost! \nTry again next time")


start_game()

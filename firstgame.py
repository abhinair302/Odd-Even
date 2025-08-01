from toss import Toss
from innings import Game
from ui import Graphics

graphics=Graphics()
graphics.head()
graphics.space()

while True:
    try:
        user_toss = input("Enter your toss (ODD/EVEN): ").strip()
        if user_toss.lower() in ["odd", "even", "o", "e"]:
            break
        else:
            print("Please enter a valid input.")
    except ValueError:
        print("Invalid input. Please enter a valid input.")

toss=Toss(user_toss)
graphics.space()

while True:
    try:
        user_chance = int(input("Enter Number between 0-6: "))
        if 0 <= user_chance <= 6:
            break
        else:
            print("Please enter a number between 0 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

toss.chance(user_chance)
if toss.winner=="User":
    while True:
        try:
            user_choice = input("Do you want to Batting or Bowling: ")
            if user_choice.lower() in ["batting", "bat", "bowling", "bowl"]:
                break
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Invalid input. Please enter a valid input.")
else:
    user_choice=toss.user_choice
comp_choice=toss.comp_choice
graphics.space()
graphics.firstinningsborder()

toss.select(user_choice)
game=Game(toss.user_choice,comp_choice)
while game.game_on:
    while True:
        try:
            user_ball = int(input("Enter Number between 0-6: "))
            if 0 <= user_ball <= 6:
                break
            else:
                print("Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    game.firstinningsmove(user_ball)
    game.firstinningscondition(user_ball)

graphics.space()
game.firstinnover()
print(f"Target for 2nd Innings is {game.firstscore+1}")
game.swap()
graphics.secondinningsborder()

graphics.space()
while game.game_on:
    while True:
        try:
            user_ball = int(input("Enter Number between 0-6: "))
            if 0 <= user_ball <= 6:
                break
            else:
                print("Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    game.secondinningsmove(user_ball)
    game.secondinningscondition(user_ball)

graphics.gameover()



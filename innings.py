from random import choice


class Game:

    def __init__(self,user_choice,comp_choice):
        self.avail_score = [0, 1, 2, 3, 4, 5, 6]
        self.firstscore=0
        self.secondscore=0
        self.comp_ball=0
        self.user_choice=user_choice
        self.comp_choice=comp_choice
        self.game_on=True


    def firstinningsmove(self,user_ball):
        self.comp_ball = choice(self.avail_score)
        print(f"Computer's move {self.comp_ball}")
        if user_ball != self.comp_ball:
            if self.user_choice == "Batting" or self.comp_choice=="Bowling":
                self.firstscore += user_ball
            else:
                self.firstscore += self.comp_ball
        print(f"Batter Score Live: {self.firstscore}")



    def firstinnover(self):
        if self.user_choice=="Batting":
            print(f"YOU ARE OUT. YOUR 1st innings score is {self.firstscore}")
        else:
            print(f"Computer is OUT. Computer's first innings score is {self.firstscore}")

    def firstinningscondition(self,user_ball):
        if user_ball == self.comp_ball:
            self.game_on = False


    def swap(self):
        if self.user_choice == "Batting":
            self.user_choice="Bowling"
        else:
            self.user_choice="Batting"
        self.game_on=True

    def secondinningsmove(self,user_ball):
        # self.comp_ball = choice(self.avail_score)
        self.comp_ball = 2
        print(f"Computer's move {self.comp_ball}")
        if user_ball != self.comp_ball:
            if self.user_choice == "Batting":
                self.secondscore += user_ball
            else:
                self.secondscore+=self.comp_ball
            if self.secondscore<=self.firstscore:
                print(f"Batter Score Live: {self.secondscore}")
                print(f"Need more {self.firstscore+1-self.secondscore} runs to win")

        elif user_ball == self.comp_ball and self.secondscore == self.firstscore:
            self.superover()

    def secondinningscondition(self,user_ball):
        if user_ball == self.comp_ball:
            if self.user_choice == "Batting" and self.secondscore < self.firstscore:
                print(f"OH, Computer Has Won The Game by {self.firstscore - self.secondscore} runs. Better Luck Next Time")
                self.game_on = False
            elif self.user_choice == "Bowling" and self.secondscore < self.firstscore:
                print(f"User Has Won The Game by {self.firstscore - self.secondscore} runs. CONGRATS")
                self.game_on = False

        elif self.user_choice == "Batting" and self.secondscore > self.firstscore:
            print("User Has Won The Game. CONGRATS")
            self.game_on = False
        elif self.user_choice == "Bowling" and self.secondscore > self.firstscore:
            print("OH, Computer Has Won The Game. Better Luck Next Time")
            self.game_on = False


    def superover(self):
        print("\n⚡ IT'S A TIE! SUPER OVER TIME! ⚡")
        print("-----------------------------------")

        # Reset scores and innings
        self.firstscore = 0
        self.secondscore = 0
        self.game_on = True

        # Swap user/computer roles
        if self.user_choice == "Batting":
            self.user_choice = "Bowling"
        else:
            self.user_choice = "Batting"

        print(f"🔁 In the Super Over, you will do: {self.user_choice}")

        # First Super Over innings
        print("\n🏏 SUPER OVER - FIRST INNINGS")
        while self.game_on:
            try:
                user_ball = int(input("Enter your chance (0-6): "))
                if 0 <= user_ball <= 6:
                    self.firstinningsmove(user_ball)
                    self.firstinningscondition(user_ball)
                else:
                    print("⚠️ Please enter a number between 0 and 6.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")

        print(f"\n🎯 Target for second innings: {self.firstscore + 1}")
        self.swap()

        # Second Super Over innings
        print("\n🏏 SUPER OVER - SECOND INNINGS")
        while self.game_on:
            try:
                user_ball = int(input("Enter your chance (0-6): "))
                if 0 <= user_ball <= 6:
                    self.secondinningsmove(user_ball)
                    self.secondinningscondition(user_ball)
                else:
                    print("⚠️ Please enter a number between 0 and 6.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")


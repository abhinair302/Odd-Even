from random import choice

class Toss:

    def __init__(self,user_toss):
        self.avail_score=[0,1,2,3,4,5,6]
        self.user_toss=user_toss
        if self.user_toss.lower() in ["odd", "o"]:
            self.comp_toss = "Even"
            print(f"You chose {self.user_toss}. Hence, Computer got {self.comp_toss}")
        else:
            self.comp_toss = "Odd"
            print(f"You chose {self.user_toss}. Hence, Computer got {self.comp_toss}")
        self.comp_chance=""
        self.winner=""
        self.comp_choice=""
        self.user_choice=""

    def chance(self,user_chance):
        self.comp_chance=choice(self.avail_score)
        print(f"Computer chose {self.comp_chance}")
        if (self.comp_chance+user_chance)%2==0:
            if self.user_toss.lower() in ["even", "e"]:
                self.winner="User"
            else:
                self.winner="Computer"

        else:
            if self.user_toss.lower() in ["odd", "o"]:
                self.winner="User"
            else:
                self.winner="Computer"
        print(f"{user_chance}+{self.comp_chance}={user_chance+self.comp_chance}")
        print(f"{self.winner} has won the toss")


    def select(self,user_choice):
        self.user_choice=user_choice
        if self.winner=="User":
            if user_choice.lower() in ["batting", "bat"]:
                self.comp_choice="Bowling"
                print(f"Hence, Computer will do {self.comp_choice}")
            else:
                self.comp_choice="Batting"
                print(f"Hence, Computer will do {self.comp_choice}")
        else:
            self.comp_choice=choice(["Batting","Bowling"])
            if self.comp_choice=="Batting":
                self.user_choice="Bowling"
                print(f"You lost the toss. Hence Computer decides to {self.comp_choice} and you will do {self.user_choice}")
            else:
                self.user_choice="Batting"
                print(f"You lost the toss. Hence Computer decides to {self.comp_choice} and you will do {self.user_choice}")







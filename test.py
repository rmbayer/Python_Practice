from random import choice


class Game:
    
    def __init__(self):
        self.cpu = Player()
        self.human = Player(True)

    
    
    def run(self):
        for i in range(5):
            if self.cpu.wins > 2 or self.human.wins > 2:
                break
            else:
                #play a hand
                self.cpu.throw()
                self.human.throw()
            self.compare_hands()
                
                
        print(f"{self.human} Score: {self.human.wins}")
        print(f"{self.cpu} Score: {self.cpu.wins}")

            
    def compare_hands(self):
        #return human or CPU
        print("CPU threw " + self.cpu.hand)
        if self.human == self.cpu:
            print("Draw")
        elif self.human < self.cpu:
            print("CPU Wins")
            self.cpu += 1
        elif self.human > self.cpu:
            print("Human Won")
            self.human += 1
        else:
            print("TERRIBLE ERROR")

            
        # Figure out who won
    
    
class Player:
    def __init__(self, human=False):
        self.human = human
        self.name = "Bob" if self.human else "computer"
        self.wins = 0
        self.hand = None
        self.choices = ["Rock", "Paper", "Scissors"]
        self.hand_to_int = {
            "Rock":2,
            "Paper":1,
            "Scissors":0
        }
        
    def throw(self):
        if self.human:
            self.hand = input("Rock, Paper, or Scissors?")
        else:
            self.hand = choice(self.choices)
            
    
    def __eq__(self, other):
        #Did we draw
        return self.hand == other.hand


    def __lt__(self, other):
        #Did we lose
        # I throw rock, cpu thros paper
        # I throw paper, cpu throws scissors
        if (self.hand == "Rock" and other.hand == "Paper" or
            self.hand == "Scissors" and other.hand =="Rock" or
            self.hand == "Paper" and other.hand == "Scissors"):
            return True
        else:
            return False
        

    def __gt__(self, other):
        # Did we Win
        if (other.hand == "Rock" and self.hand == "Paper" or
            other.hand == "Scissors" and self.hand =="Rock" or
            other.hand == "Paper" and self.hand == "Scissors"):
            return True
        else:
            return False
        
    def __add__(self, other):
        self.wins += other
        return self


    def __repr__(self):
        return f"{self.name} has won {self.wins} times"

    def __str__(self):
        return self.name
    
    


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()




# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         x = list(func())
#         print("Something is happening after the function is called.")
#         return x

#     return wrapper

# @my_decorator
# def say_whee():
#     return ("Whee!")

# print(say_whee())

# def main():
#     game = Game()
#     game.run()
#
#
# if __name__ == '__main__':
#     main()

            














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
            # who won the hand
            # rock beats scissors
            # scissors beats paper
            # paper beats rock
            # there can be a tie
            
    def compare_hands(self):
        #return human or CPU
        if self.human == self.cpu:
            #draw
            
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
        return self.hand == other.hand

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __repr__(self):
        return f"{self.name} has won {self.wins} times"

    def __str__(self):
        return self.name


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        x = list(func())
        print("Something is happening after the function is called.")
        return x

    return wrapper

@my_decorator
def say_whee():
    return ("Whee!")

print(say_whee())

# def main():
#     game = Game()
#     game.run()
#
#
# if __name__ == '__main__':
#     main()

            
    
def main():
    game = Game()
    game.run()
    
    
    
if __name__ == '__main__':
    main()














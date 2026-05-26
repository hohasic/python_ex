import random

class Dice:
    def __init__(self):
        self.nembers = []

    def playDice(self):
        self.nembers.append(random.randint(1, 6))

    def getNumbers(self):
        return self.nembers
    
    def getSum(self):
        return sum(self.nembers)
    
class ResaleShop:
    inventory: list = []

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    
    def buy(self, computer):
        self.inventory.append(computer)
        return computer
    
    def sell(self, computer):
        self.inventory.remove(computer)
        return True
    




    # What methods will you need?
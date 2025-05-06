class ResaleShop:
    inventory: list = []

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    #constructor for resale shop
    def __init__(self):
        self.inventory = []
    
    #appending newly bought computer to inventory
    def buy(self, computer):
        self.inventory.append(computer)
        return computer
    
    #method to sell computer; checks if computer is in inventory before selling it
    def sell(self, computer):
        if computer in self.computer:
            self.inventory.pop(computer)
            print("Item sold!")
        else: 
            print("Item not found. Please select another item to sell.")
    
    #method to print inventory 
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for item in self.inventory:
            # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")



    # What methods will you need?
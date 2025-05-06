class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    #constructor for computer
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: str, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # What methods will you need?

    #method to change the  price of a computer
    def changePrice(self, newPrice:int):
        self.price = newPrice

    #method to update operating system of computer
    def changeOS(self, newOS:int):
        self.operating_system = newOS
    
    #pricing a refurbished computer, updating price based on its year
    def refurbish(self):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000


    
    
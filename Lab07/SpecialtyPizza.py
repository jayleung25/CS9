from Pizza import Pizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.size = size
        self.name = name
        if self.size == "S":
            self.setPrice(12)
        elif self.size == "M":
            self.setPrice(14)
        else:
            self.setPrice(16)

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: " + self.size + "\nName: " + self.name + f"\nPrice: ${'{:.2f}'.format(self.getPrice())}\n"
    
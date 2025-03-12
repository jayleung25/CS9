from Pizza import Pizza

class CustomPizza(Pizza):

    def __init__(self, size):
        super().__init__(size)
        self.toppingsList = []
        self.fixedPrice()

    def fixedPrice(self):
        if self.size == "S":
            self.setPrice(8)
        elif self.size == "M":
            self.setPrice(10)
        else:
            self.setPrice(12)

    def addTopping(self, topping):
        if self.size == "S":
            self.toppingsList.append(topping)
            self.setPrice(self.getPrice() + 0.5)
        elif self.size == "M":
            self.toppingsList.append(topping)
            self.setPrice(self.getPrice() + 0.75)
        else:
            self.toppingsList.append(topping)
            self.setPrice(self.getPrice() + 1)

    def getPizzaDetails(self):
        pizzaString = "CUSTOM PIZZA\nSize: " + self.size + "\nToppings:\n"
        x = 0
        while x < len(self.toppingsList):
            pizzaString += f"\t+ {self.toppingsList[x]}\n"
            x += 1
        pizzaString += f"Price: ${'{:.2f}'.format(self.getPrice())}\n"
        return pizzaString
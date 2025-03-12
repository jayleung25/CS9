from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:

    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
    
    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        pizzaString = "******\nOrder Time: " + str(self.time) + "\n" 
        x = 0
        totalPrice = 0
        while x < len(self.pizzas):
            pizzaString += self.pizzas[x].getPizzaDetails() + "\n----\n"
            totalPrice += self.pizzas[x].getPrice()
            x += 1
        pizzaString += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(totalPrice)
        return pizzaString
    
    def __lt__(self, rhs):
        if self.getTime() < rhs.getTime():
            return True
        else:
            return False
    
    def __gt__(self, rhs):
        if self.getTime() > rhs.getTime():
            return True
        else:
            return False
        
    def __eq__(self, rhs):
        return self.getTime() == rhs.getTime()
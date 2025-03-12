class Car:

    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price > rhs.price
                else:
                    return self.year > rhs.year
            else:
                return self.model > rhs.model
        else:
            return self.make > rhs.make
        return False
    
    def __lt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price < rhs.price
                else:
                    return self.year < rhs.year
            else:
                return self.model < rhs.model
        else:
            return self.make < rhs.make
        return False
    
    def __eq__(self, rhs):
        return self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price == rhs.price
    
    def __str__(self):
        return "Make: " + self.make + ", Model: " + self.model + ", Year: " + str(self.year) + ", Price: $" + str(self.price)
    

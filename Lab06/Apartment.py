class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return "(Apartment) Rent: $" + str(self.rent) + ", Distance From UCSB: "  + str(self.metersFromUCSB)  + "m, Condition: " + self.condition

    '''def __lt__(self, rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and (self.condition == "excellent" and rhs.condition == "bad" or rhs.condition == "average") or (self.condition == "average" and rhs.condition == "bad"):
            return True
        elif self.rent == rhs.rent and self.metersFromUCSB < rhs.metersFromUCSB:
            return True
        elif self.rent < rhs.rent:
            return True
        else:
            return False
        
    def __gt__(self, rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and (self.condition == "bad" and rhs.condition == "excellent" or rhs.condition == "average") or (self.condition == "average" and rhs.condition == "excellent"):
            return True
        elif self.rent == rhs.rent and self.metersFromUCSB > rhs.metersFromUCSB:
            return True
        elif self.rent > rhs.rent:
            return True
        else:
            return False'''
        
    def __eq__(self, rhs):
        return self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition
    
    def __lq__(self, rhs):
        theList = ["excellent", "average", "bad"]
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                return theList.index(self.condition) < theList.index(rhs.condition)
            else:
                return self.metersFromUCSB < rhs.metersFromUCSB
        else:
            return self.rent < rhs.rent

    def __gt__(self, rhs):
        theList = ["excellent", "average", "bad"]
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                return theList.index(self.condition) > theList.index(rhs.condition)
            else:
                return self.metersFromUCSB > rhs.metersFromUCSB
        else:
            return self.rent > rhs.rent
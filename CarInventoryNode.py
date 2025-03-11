class CarInventoryNode:

    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right

    def spliceOut(self):
    #leaf node
        if self.getRight() is None and self.getLeft() is None:
            if self.parent.getLeft() is self:
                self.getParent().setLeft(None)
            else:
                self.getParent().setRight(None)
        #one right child
        elif self.getRight() is not None:
            if self.getParent().getLeft() is self:
                self.getParent().setLeft(self.getRight())
            else:
                self.getParent().setRight(self.getRight())
            self.getRight().setParent(self.getParent())

    def __str__(self):
        retVal = ""
        for i in self.cars:
            retVal += str(i) + "\n"
        return retVal
    
    def __gt__(self, rhs):
        if self.make == rhs.make:
            return self.model > rhs.model
        else:
            return self.make > rhs.make

    def __lt__(self, rhs):
        if self.make == rhs.make:
            return self.model < rhs.model
        else:
            return self.make < rhs.make

    def __eq__(self, rhs):
        return (self.make == rhs.make) and (self.model == rhs.model)
    
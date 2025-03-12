from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            self._addCar(CarInventoryNode(car), self.root)
        else:
            self.root = CarInventoryNode(car)
            
    def _addCar(self, newNode, currentNode):
        if newNode == currentNode:
            currentNode.cars.append(newNode.cars[0])
        elif newNode < currentNode:
            if currentNode.getLeft():
                self._addCar(newNode,currentNode.getLeft())
            else:
                currentNode.setLeft(newNode)
                newNode.setParent(currentNode)
        else:
            if currentNode.getRight():
                self._addCar(newNode, currentNode.getRight())
            else:
                currentNode.setRight(newNode)
                newNode.setParent(currentNode)

    def preOrder(self):
        return self._preOrder(self.root)
        
    def _preOrder(self, theRoot):
        ret = ""
        if theRoot is not None:
            ret += str(theRoot)
            ret += self._preOrder(theRoot.getLeft())
            ret += self._preOrder(theRoot.getRight())
        return ret
    
    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, theRoot):
        ret = ""
        if theRoot is not None:
            ret += self._inOrder(theRoot.getLeft())
            ret += str(theRoot)
            ret += self._inOrder(theRoot.getRight())
        return ret
    
    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, theRoot):
        ret = ""
        if theRoot is not None:
            ret += self._postOrder(theRoot.getLeft())
            ret += self._postOrder(theRoot.getRight())
            ret += str(theRoot)
        return ret
    

    def doesCarExist(self, car):
        currentNode = self.root
        while currentNode is not None:
            if currentNode == car:
                for i in currentNode.cars:
                    if i == car:
                        return True
                return False
            elif currentNode > car:
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
        return False
    
    def getTotalInventoryPrice(self):
        return self.totalInventoryPrice(self.root)
    
    def totalInventoryPrice(self, currentNode):
        totalPrice = 0
        if currentNode is None:
            return totalPrice
        if currentNode is not None:
            totalPrice += self.totalInventoryPrice(currentNode.getLeft())
            for i in currentNode.cars:
                totalPrice += i.price
            totalPrice += self.totalInventoryPrice(currentNode.getRight())
        return totalPrice
      
    def getBestCar(self, make, model):
        newNode = self._getBestCar(self.root, make, model)
        if newNode is None:
            return None
        theValue = newNode.cars[0]
        for i in newNode.cars:
            if i > theValue:
                theValue = i
        return theValue
        
    def _getBestCar(self, current, make, model):
        while current is not None:
            if current.getMake() == make.upper() and current.getModel() == model.upper():
                return current
            elif current.getMake() > make.upper():
                current = current.getLeft()
            elif current.getMake() < make.upper():
                current = current.getRight()
            elif current.getMake() == make.upper() and current.getModel() > model.upper():
                current = current.getLeft()
            else:
                current = current.getRight()
        return None

    def getWorstCar(self, make, model):
        newNode = self._getBestCar(self.root, make, model)
        if newNode is None:
            return None
        theValue = newNode.cars[0]
        for i in newNode.cars:
            if i < theValue:
                theValue = i
        return theValue
        
    def _getWorstCar(self, current, make, model):
        while current is not None:
            if current.getMake() == make.upper() and current.getModel() == model.upper():
                return current
            elif current.getMake() > make.upper():
                current = current.getLeft()
            elif current.getMake() < make.upper():
                current = current.getRight()
            elif current.getMake() == make.upper() and current.getModel() > model.upper():
                current = current.getLeft()
            else:
                current = current.getRight()
        return None
        
    def removeCar(self, make, model, year, price):
        return self._removeCar(self.root, make, model, year, price)
    
    def _removeCar(self, current, make, model, year, price):
        if current is None:
            return False
        elif current.getMake() == make.upper() and current.getModel() == model.upper():
            for i in range(len(current.cars)):
                if current.cars[i].year == year and current.cars[i].price == price:
                    current.cars.pop(i)
                    if len(current.cars) == 0:
                        #leaf node
                        if current.getLeft() is None and current.getRight() is None:
                            if current.getParent() is None:
                                self.root = None
                                return True
                            elif current.getParent().getLeft() is current:
                                current.getParent().setLeft(None)
                                return True
                            else:
                                current.getParent().setRight(None)
                                return True
                        #one child
                        elif (current.getLeft() is None and current.getRight() is not None) or (current.getLeft() is not None and current.getRight() is None):
                            if current.getLeft() is None:
                                if current.getParent() is None:
                                    self.root == current.getRight()
                                    current.getRight().setParent(None)
                                    return True
                                elif current.getParent().getRight() is current:
                                    current.getParent().setRight(current.getRight())
                                    current.getRight().setParent(current.getParent())
                                    return True
                                else:
                                    current.getParent().setLeft(current.getRight())
                                    current.getRight().setParent(current.getParent())
                                    return True
                            else:
                                if current.getParent() is None:
                                    self.root == current.getLeft()
                                    current.getLeft().setParent(None)
                                    return True
                                elif current.getParent().getRight() is current:
                                    current.getParent().setRight(current.getLeft())
                                    current.getLeft().setParent(current.getParent())
                                    return True
                                else:
                                    current.getParent().setLeft(current.getLeft())
                                    current.getLeft().setParent(current.getParent())
                                    return True
                        #both children
                        else:
                            changeNode = self._getSuccessor(current, current.getMake(), current.getModel())
                            changeNode.spliceOut()
                            current = changeNode
                            return True
                    return True
            return False
        elif current.getMake() > make.upper():
            return self._removeCar(current.getLeft(), make, model, year, price)
        elif current.getMake() == make.upper() and current.getModel() > model.upper():
            return self._removeCar(current.getLeft(), make, model, year, price)
        else:
            return self._removeCar(current.getRight(), make, model, year, price)
        return False

    def getSuccessor(self, make, model):
        return self._getSuccessor(self.root, make, model)
    
    def _getSuccessor(self, current, make, model):
        while current is not None:
            if current.getMake() == make.upper() and current.getModel() == model.upper():
                if current.getRight() is not None:
                    current = current.getRight()
                    return self.findMin(current)
                else:
                    if current.getParent() is None:
                        return None
                    else:
                        while current.getParent() is not None:
                            if current.getParent() > current:
                                return current.getParent()
                            else:
                                current = current.getParent()

                        return None
            elif current.cars[0].make > make.upper():
                current = current.getLeft()
            elif current.cars[0].make == make.upper() and current.cars[0].model > model.upper():
                current = current.getLeft()
            else:
                current = current.getRight()
        return None
    
    def findMin(self, current):
        while current.getLeft() is not None:
            current = current.getLeft()
        return current

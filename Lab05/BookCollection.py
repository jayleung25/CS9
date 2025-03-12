from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection:
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        '''
        b = BookCollectionNode(book)
        if self.isEmpty() or self.head.getData() > book or book == self.head.getData():
            b.setNext(self.head)
            self.head = b
            return
        else:
            temp = self.head
            while temp != None:
                if book > temp.getData() or book == temp.getData():
                    nextNode = temp.getNext()
                    temp.setNext(b)
                    b.setNext(nextNode)
                    return
                temp = temp.getNext()'''
        b = BookCollectionNode(book)
        if self.isEmpty() or self.head.getData() > book or book == self.head.getData():
            b.setNext(self.head)
            self.head = b
            return
        else:
            temp1 = self.head
            temp2 = temp1.getNext()
            while temp2 != None:
                if book > temp2.getData():
                    temp1 = temp2
                    temp2 = temp2.getNext()
                    if temp2 == None:
                        temp1.setNext(b)
                        return
                else:
                    temp1.setNext(b)
                    b.setNext(temp2)
                    return
            self.head.setNext(b)
                        
                

    def getBooksByAuthor(self, author):
        temp = self.head
        fullList = ""
        while temp != None:
            if temp.getData().getAuthor().lower() == author.lower():
                fullList += temp.getData().getBookDetails() + "\n"
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return fullList
    
    def getAllBooksInCollection(self):
        temp = self.head
        fullList = ""
        while temp != None:
            fullList += temp.getData().getBookDetails() + "\n"
            temp = temp.getNext()
        return fullList

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode != None and bookNode.getData().getTitle().lower() != title.lower():
            return self.recursiveSearchTitle(title, bookNode.getNext())
        elif bookNode != None and bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return False

    def removeAuthor(self, author):
        if self.isEmpty():
            return
        while self.isEmpty() == False and self.head.getData().getAuthor().lower() == author.lower():
            self.head = self.head.getNext()
        if self.isEmpty():
            return
        current = self.head
        removalNode = self.head.getNext()
        if removalNode == None:
                        return
        while removalNode != None and removalNode.getData().getAuthor().lower() != author.lower():
            current = removalNode
            removalNode = removalNode.getNext()
        while removalNode !=None and removalNode.getData().getAuthor().lower() == author.lower():
            removalNode = removalNode.getNext()
        current.setNext(removalNode)
        '''nextNode = removalNode.getNext()
        while removalNode != None:
            if removalNode.getData().getAuthor().lower() == author.lower():
                current.setNext(nextNode)
                current = current.getNext()
                removalNode = current.getNext()
                if removalNode == None:
                        return
                nextNode = removalNode.getNext()
            else:
                current = removalNode
                removalNode = nextNode
                if removalNode == None:
                        return
                nextNode = removalNode.getNext()'''




        '''if self.isEmpty():
            return
        while self.isEmpty() == False and self.head.getData().getAuthor().lower() == author.lower():
            self.head = self.head.getNext()
            if self.head.getNext() != None and self.head.getData().getAuthor().lower() == author.lower():
                self.head.getNext() == self.head.getNext().getNext()
            else:
                return
        if self.isEmpty():
            return
        previous = self.head
        current = self.head.getNext()
        removalNode = self.head.getNext().getNext()
        if removalNode == None:
                        return
        nextNode = removalNode.getNext()
        while removalNode != None:
            if removalNode.getData().getAuthor().lower() == author.lower():
                current.setNext(nextNode)
                current = current.getNext()
                removalNode = current.getNext()
                if removalNode == None:
                        return
                nextNode = removalNode.getNext()
            else:
                current = removalNode
                removalNode = nextNode
                if removalNode == None:
                        return
                nextNode = removalNode.getNext()'''


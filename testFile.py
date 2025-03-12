from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def testBookClass():
    a = Book("Book 1", "Jay L.", 1999)
    assert a.getTitle() == "Book 1"
    assert a.getAuthor() == "Jay L."
    assert a.getYear() == 1999
    assert a.getBookDetails() == "Title: Book 1, Author: Jay L., Year: 1999"

def testBookCollectionNodeClass():
    a = Book("Book 1", "Jay L.", 1999)
    b = Book("Book 2", "Daniel Y.", 2000)
    c = BookCollectionNode(a)
    d = BookCollectionNode(b)
    assert c.getData().getBookDetails() == a.getBookDetails()
    c.setNext(d)
    assert c.getNext().getData().getBookDetails() == d.getData().getBookDetails()
    c.setData(b)
    assert c.getData().getBookDetails() == b.getBookDetails()

def testBookCollectionClass():
    a = Book("Book 1", "Jay L.", 1999)
    b = Book("Book 2", "Daniel Y.", 2000)
    c = Book("Book 3", "Jay L.", 3000)
    d = Book("Book 4", "Casey K.", 1000)
    f = Book("Book 5", "Jay L.", 1999)
    g = Book("Book 1", "Jay L.", 1999)
    e = BookCollection()
    assert e.isEmpty() == True
    e.insertBook(a)
    e.insertBook(b)
    e.insertBook(c)
    e.insertBook(d)
    e.insertBook(f)
    e.insertBook(g)
    assert e.isEmpty() == False
    assert e.getNumberOfBooks() == 6
    assert a > b
    assert c > a
    assert f > a
    assert e.getAllBooksInCollection() == "Title: Book 4, Author: Casey K., Year: 1000\nTitle: Book 2, Author: Daniel Y., Year: 2000\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 5, Author: Jay L., Year: 1999\nTitle: Book 3, Author: Jay L., Year: 3000\n"
    assert e.getBooksByAuthor("Jay L.") == "Title: Book 1, Author: Jay L., Year: 1999\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 5, Author: Jay L., Year: 1999\nTitle: Book 3, Author: Jay L., Year: 3000\n"
    e.removeAuthor("Daniel Y.")
    assert e.getAllBooksInCollection() == "Title: Book 4, Author: Casey K., Year: 1000\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 5, Author: Jay L., Year: 1999\nTitle: Book 3, Author: Jay L., Year: 3000\n"
    e.removeAuthor("Jay L.")
    assert e.getAllBooksInCollection() == "Title: Book 4, Author: Casey K., Year: 1000\n"
    e.insertBook(a)
    e.insertBook(b)
    e.insertBook(c)
    e.insertBook(f)
    e.insertBook(g)
    assert e.getAllBooksInCollection()  == "Title: Book 4, Author: Casey K., Year: 1000\nTitle: Book 2, Author: Daniel Y., Year: 2000\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 1, Author: Jay L., Year: 1999\nTitle: Book 5, Author: Jay L., Year: 1999\nTitle: Book 3, Author: Jay L., Year: 3000\n"
    assert e.recursiveSearchTitle("Book 4", e.head) == True
    assert e.recursiveSearchTitle("Book 5", e.head) == True
    assert e.recursiveSearchTitle("ASJIHDS", e.head) == False
    
testBookClass()
testBookCollectionNodeClass()
testBookCollectionClass()

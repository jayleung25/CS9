class Book:

    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Year: " + str(self.year)

    def __gt__(self, rhs):
        if self.author.lower() > rhs.author.lower():
            return True
        elif self.author.lower() == rhs.author.lower() and self.year > rhs.year:
            return True
        elif self.author.lower() == rhs.author.lower() and self.year == rhs.year and self.title.lower() > rhs.title.lower():
            return True
        else:
            return False

    def __eq__(self, rhs):
        if self.author.lower() == rhs.author.lower() and self.title.lower() == rhs.title.lower() and self.year == rhs.year:
            return True
        else:
            return False

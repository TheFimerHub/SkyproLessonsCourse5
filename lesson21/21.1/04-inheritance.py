
#01-inheritance.py

class Book:
    def __init__(self, name, pages, content, author):
        self.name = name
        self.pages = pages
        self.content = content
        self.author = author

class Ebook(Book):
    def __init__(self, name, pages, content, author, links):
        super().__init__(name, pages, content, author)
        self.links = links

book_1 = Book("The Hobbit", 100, "This is a book", "John Doe")
E_book = Book("The Hobbit", 100, "This is a book", "John", ["https://www.ebooker.com/book/006.pdf"])


#02-override.py

class StoreItem:
    def calculate(self, count):
        return self.calculate_tax(count) + (count * 100)

    def _calculate_tax(self, count):
        return 0

class StoreItemInternational(StoreItem):
    def _calculate_tax(self, count):
        return count * 0.5

item = StoreItemInternational()
item.calculate(10)


#03-inheritance-chain.py

class PrintedProduct:
    def __init__(self, name, pages, content):
        self.name = name
        self.pages = pages
        self.content = content

class Book:
    def __init__(self, name, pages, content, author):
        self.name = name
        self.pages = pages
        self.content = content
        self.author = author

class Magazine(PrintedProduct):
    def __init__(self, name, pages, content):
        super().__init__(name, pages, content)
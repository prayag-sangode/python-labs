# Lab 3.11: Magic Methods – __str__, __len__, __add__

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Magic method to customize print()
    def __str__(self):
        return f"Book: '{self.title}', Pages: {self.pages}"

    # Magic method to use len() on a Book
    def __len__(self):
        return self.pages

    # Magic method to use + to combine two books
    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

# Create book objects
book1 = Book("Python Basics", 150)
book2 = Book("OOP with Python", 100)

# __str__ allows clean printing
print(book1)
print(book2)

# __len__ allows us to use len()
print("Pages in book1:", len(book1))
print("Pages in book2:", len(book2))

# __add__ allows book1 + book2
combo = book1 + book2
print("Combined book:", combo)
print("Total pages in combo:", len(combo))

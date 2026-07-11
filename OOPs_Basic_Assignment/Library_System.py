class Library:
    def __init__(self,name,author,is_available,quantity):
        self.name = name
        self.author = author
        self.is_available = is_available
        self.quantity = quantity

    def display(self):
        print("Book Details:")
        print("="*20)
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Is_Available: {self.is_available}")
        print(f"Quantity: {self.quantity}")
        print(f"{'='*20}\n")

    def add_book(self, quantity):
        self.is_available = True if self.quantity > 0 else False
        print(f"{quantity} copies of '{self.name}' added to the library.")

    def remove_book(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            self.is_available = True if self.quantity > 0 else False
            print(f"{quantity} copies of '{self.name}' removed from the library.")
        else:
            print("Not enough books available in the library.")

books = [
    Library("The Great Gatsby", "F. Scott Fitzgerald", True, 5),
    Library("To Kill a Mockingbird", "Harper Lee", True, 3),
    Library("1984", "George Orwell", False, 0)]

for book in books:
    book.display()

added_books = [
    Library("Pride and Prejudice", "Jane Austen", True, 2),
    Library("The Catcher in the Rye", "J.D. Salinger", True, 6)]

for book in added_books:
    book.add_book(book.quantity)
    book.display()

removed_books = [
    Library("The Great Gatsby", "F. Scott Fitzgerald", True, 2),
    Library("To Kill a Mockingbird", "Harper Lee", True, 1)]

for book in removed_books:
    book.remove_book(book.quantity)
    book.display()
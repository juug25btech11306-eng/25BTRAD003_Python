import csv, os
FILE = "library.csv"
class Book:
    def __init__(self, title, author, status="Available"):
        self.title, self.author, self.status = title, author, status
class Library:
    def __init__(self): self.books = []; self.load_books()
    def load_books(self):
        if os.path.exists(FILE):
            with open(FILE, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f): self.books.append(Book(row["Title"], row["Author"], row["Status"]))
    def save_books(self):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["Title", "Author", "Status"])
            for b in self.books: w.writerow([b.title, b.author, b.status])
    def add_book(self):
        title, author = input("Book title: ").strip(), input("Author: ").strip()
        if not title or not author: print("Title and author cannot be empty!"); return
        self.books.append(Book(title, author)); self.save_books(); print("Book added.")
    def issue_book(self):
        title = input("Book title to issue: ").strip().lower()
        for b in self.books:
            if b.title.lower() == title:
                if b.status == "Available": b.status = "Issued"; self.save_books(); print("Book issued.")
                else: print("Book is already issued.")
                return
        print("Book not found!")
    def return_book(self):
        title = input("Book title to return: ").strip().lower()
        for b in self.books:
            if b.title.lower() == title:
                if b.status == "Issued": b.status = "Available"; self.save_books(); print("Book returned.")
                else: print("Book was not issued.")
                return
        print("Book not found!")
    def display_books(self):
        if not self.books: print("No books available.")
        for b in self.books: print(b.title, "|", b.author, "|", b.status)
if __name__ == "__main__":
    library = Library()
    while True:
        c = input("\n1.Add 2.Issue 3.Return 4.Display 5.Exit: ")
        if c == "1": library.add_book()
        elif c == "2": library.issue_book()
        elif c == "3": library.return_book()
        elif c == "4": library.display_books()
        elif c == "5": break
        else: print("Invalid choice!")

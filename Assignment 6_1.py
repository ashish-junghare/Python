class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def display(self):
        print("Book Name: ", self.Name)
        print("Author Name: ", self.Author)
        print("Number of books: ", self.NoOfBooks)


def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.display()

    obj2 = BookStore("C programming", "Dennis Ritchie")
    obj2.display()


if __name__ == "__main__":
    main()
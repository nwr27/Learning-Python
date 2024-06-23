class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        
    def borrow_book(self):
        self.available = False
        print("Buku dipinjam")

    def return_book(self):
        self.available = True
        print("Buku dikembalikan")

    def display_info(self):
        print(f"Judul: {self.title}")
        print(f"Penulis: {self.author}")
        print(f"Tahun terbit: {self.year}")
        print(f"Ketersediaan: {self.available}")

# Membuat instance dari kelas Book
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

# Menampilkan informasi buku
book1.display_info()
book2.display_info()

# Meminjam buku
book1.borrow_book()
book1.display_info()

# Mengembalikan buku
book1.return_book()
book1.display_info()

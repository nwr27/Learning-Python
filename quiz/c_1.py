class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        
    def borrow_book(self):
        if self.available:
            self.available = False
            print("Buku dipinjam")
        else:
            print("Buku sudah dipinjam dan tidak tersedia saat ini")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Buku dikembalikan")
        else:
            print("Buku sudah tersedia di perpustakaan")

    def display_info(self):
        print(f"Judul: {self.title}")
        print(f"Penulis: {self.author}")
        print(f"Tahun terbit: {self.year}")
        status = "Tersedia" if self.available else "Tidak Tersedia"
        print(f"Ketersediaan: {status}")

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

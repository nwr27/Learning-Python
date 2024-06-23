class LibraryItem:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow_item(self):
        if self.available:
            self.available = False
            print("Item dipinjam")

    def return_item(self):
        if not self.available:
            self.available = True
            print("Item dikembalikan")

    def display_info(self):
        print(f"Judul: {self.title}")
        print(f"Pengarang: {self.author}")
        print(f"Tahun terbit: {self.year}")
        status = "Tersedia" if self.available == True else "Dipinjam"
        print(f"Ketersediaan: {status}")


class Book(LibraryItem):
    pass


class Ebook(LibraryItem):
    def __init__(self, title, author, year, file_size, format, available=True):
        super().__init__(title, author, year, available)
        self.file_size = file_size
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Ukuran file: {self.file_size} MB")
        print(f"Format: {self.format}")


class Magazine(LibraryItem):

    def __init__(self, title, author, year, issue_number, month, available=True):
        super().__init__(title, author, year, available)
        self.issue_number = issue_number
        self.month = month

    def display_info(self):
        super().display_info()
        print(f"Nomor Edisi: {self.issue_number}")
        print(f"Bulan Terbit: {self.month}")


def search_by_title(library_items, title):
    found = False
    for item in library_items:
        if item.title == title:
            found = True
            break
    if found == True:
        print(f"> Item berjudul \"{title}\" ditemukan dengan info sebagai berikut:")
        item.display_info()
    else:
        print(f"> Item berjudul \"{title}\" tidak ditemukan")


# Membuat instance dari kelas Book, Ebook, dan Magazine
book1 = Book("1984", "George Orwell", 1949)
ebook1 = Ebook("Digital Fortress", "Dan Brown", 1998, 1.2, "PDF")
magazine1 = Magazine("National Geographic", "Various Authors", 2021, 150, "March")

# Menampilkan informasi item
book1.display_info()
ebook1.display_info()
magazine1.display_info()
print()

# Meminjam dan mengembalikan item
book1.borrow_item()
book1.display_info()
print()

ebook1.borrow_item()
ebook1.display_info()
print()

book1.return_item()
book1.display_info()
print()

ebook1.return_item()
ebook1.display_info()
print("=" * 30)

# Mencari item di perpustakaan
library_items = [book1, ebook1, magazine1]
search_by_title(library_items, "1984")
search_by_title(library_items, "The Great Gatsby")
print()

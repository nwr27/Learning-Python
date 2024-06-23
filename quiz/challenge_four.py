class LibraryItems:
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


class Book(LibraryItems):
    pass


class Ebook(LibraryItems):
    def __init__(self, title, author, year, file_size, format, available=True):
        super().__init__(title, author, year, available)
        self.file_size = file_size
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Ukuran file: {self.file_size} MB")
        print(f"Format: {self.format}")


class Magazine(LibraryItems):
    def __init__(self, title, author, year, issue_number, month, available=True):
        super().__init__(title, author, year, available)
        self.issue_number = issue_number
        self.month = month

    def display_info(self):
        super().display_info()
        print(f"Nomor edisi: {self.issue_number}")
        print(f"Format: {self.month}")


def search_by_title(library_items, title):
    found = False
    for item in library_items:
        if item.title.lower() == title.lower():
            found = True
            break
    if found == True:
        print(f"> Item berjudul '{title}' ditemukan")
        item.display_info()
    else:
        print(f"> Item berjudul '{title}' tidak ditemukan")


def remove_by_title(library_items, title):
    found = False
    for item in library_items:
        if item.title.lower() == title.lower():
            found = True
            break
    if found == True:
        print(f"> Item berjudul '{title}' berhasil dihapus")
        library_items.remove(item)
    else:
        print(f"> Item berjudul '{title}' tidak ditemukan")


def list_all_items(library_items):
    for item in library_items:
        item.display_info()


# Membuat instance dari kelas Book, Ebook, dan Magazine
book1 = Book("1984", "George Orwell", 1949)
ebook1 = Ebook("Digital Fortress", "Dan Brown", 1998, 1.2, "PDF")
magazine1 = Magazine("National Geographic", "Various Authors", 2021, 150, "March")

# Menambahkan item ke daftar perpustakaan
library_items = [book1, ebook1, magazine1]

# Menampilkan semua item di perpustakaan
list_all_items(library_items)
print()

# Meminjam dan mengembalikan item
book1.borrow_item()
ebook1.borrow_item()
book1.return_item()
ebook1.return_item()
print()

# Mencari item di perpustakaan
search_by_title(library_items, "1984")
search_by_title(library_items, "The Great Gatsby")
print()

# Menghapus item dari perpustakaan
remove_by_title(library_items, "1984")
remove_by_title(library_items, "The Great Gatsby")
print()

# Menampilkan semua item di perpustakaan setelah penghapusan
list_all_items(library_items)
print()

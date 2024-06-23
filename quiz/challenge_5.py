class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Nama item: {self.name}")
        print(f"Harga item: ${self.price}")


class Product(Item):

    def __init__(self, name, price, stock):
        super().__init__(name, price)
        self.stock = stock

    def update_stock(self, quantity):
        self.stock = quantity
        pass

    def display_info(self):
        super().display_info()
        print(f"Stok: {self.stock} pcs")


class Service(Item):
    def __init__(self, name, price, duration):
        super().__init__(name, price)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Durasi layanan: {self.duration} jam")


class CashierSystem:
    def __init__(self, items=None, transactions=None):
        self.items = items if items is not None else []
        self.transactions = transactions if transactions is not None else []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Item '{name}' berhasil dihapus")
                return
        print(f"Item '{name}' tidak ditemukan")

    def search_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"Item '{name}' ditemukan:")
                item.display_info()
                return
        print(f"Item '{name}' tidak ditemukan")

    def update_stock(self, name, quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                if isinstance(item, Product):
                    item.update_stock(item.stock + quantity)
                break

    def sell_item(self, name, quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                if isinstance(item, Product) and item.stock >= quantity:
                    item.update_stock(item.stock - quantity)
                    self.transactions.append((name, quantity, item.price * quantity))
                    print(f"Berhasil menjual {quantity} {name}(s)")
                    return
                elif isinstance(item, Service):
                    self.transactions.append((name, quantity, item.price * quantity))
                    print(f"Berhasil menjual {quantity} layanan {name}")
                    return
                else:
                    print(f"Stok '{name}' tidak mencukupi")
                    return
        print(f"Item '{name}' tidak ditemukan")

    def generate_report(self):
        print("--- Laporan Penjualan ---")
        total_sales = 0
        for transaction in self.transactions:
            name, quantity, total = transaction
            print(f"{quantity} x {name} = ${total}")
            total_sales += total
        print(f"Total Penjualan: {total_sales}")

    def list_all_items(self):
        for item in self.items:
            item.display_info()


# Membuat instance dari kelas Product dan Service
product1 = Product("Laptop", 1000, 10)
product2 = Product("Mouse", 25, 100)
service1 = Service("Repair", 50, 2)

# Membuat instance dari kelas CashierSystem
cashier = CashierSystem()

# Menambahkan item ke sistem kasir
cashier.add_item(product1)
cashier.add_item(product2)
cashier.add_item(service1)

# Menampilkan semua item di sistem kasir
cashier.list_all_items()

# Memperbarui stok item
cashier.update_stock("Laptop", 5)
cashier.update_stock("Mouse", -20)

# Menjual item
cashier.sell_item("Laptop", 2)
cashier.sell_item("Mouse", 10)
cashier.sell_item("Repair", 1)

# Mencari item di sistem kasir
cashier.search_item("Laptop")
cashier.search_item("Keyboard")  # Item tidak ada

# Menghapus item dari sistem kasir
cashier.remove_item("Repair")

# Menampilkan semua item di sistem kasir setelah penghapusan
cashier.list_all_items()

# Menghasilkan laporan penjualan
cashier.generate_report()

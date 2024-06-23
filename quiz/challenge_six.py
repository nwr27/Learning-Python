class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Nama barang: {self.name}")
        print(f"Harga barang: ${self.price}")
        print(f"Jumlah barang: {self.quantity} pcs")


class Electronic(InventoryItem):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Merek: {self.brand}")


class Furniture(InventoryItem):
    def __init__(self, name, price, quantity, material):
        super().__init__(name, price, quantity)
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Bahan: {self.material}")


class Warehouse:
    def __init__(self, items=None, sold_items=None):
        self.items = items if items is not None else []
        self.sold_items = sold_items if sold_items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Item '{name}' berhasil dihapus")
                return
        else:
            print(f"Item '{name}' tidak ditemukan")

    def sell_item(self, name, quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    self.sold_items.append((item, quantity))
                    print(f"Berhasil menjual {quantity} {name}")
                else:
                    print(f"Stok '{name}' tidak mencukupi")
                return
        print(f"Item '{name}' tidak ditemukan")

    def list_all_items(self):
        for item in self.items:
            item.display_info()

    def list_sold_items(self):
        for item, quantity in self.sold_items:
            print(f"{item.name} sejumlah {quantity} terjual dengan harga: ${item.price*quantity}")


# Membuat instance dari kelas Electronic dan Furniture
electronic1 = Electronic("Laptop", 1000, 20, "Dell")
electronic2 = Electronic("Smartphone", 500, 50, "Samsung")
furniture1 = Furniture("Chair", 150, 30, "Wood")

# Membuat instance dari kelas Warehouse
warehouse = Warehouse()

# Menambahkan item ke gudang
warehouse.add_item(electronic1)
warehouse.add_item(electronic2)
warehouse.add_item(furniture1)

# Menampilkan semua item di gudang
warehouse.list_all_items()
print()

# Menjual item
warehouse.sell_item("Laptop", 5)
warehouse.sell_item("Chair", 10)
print()

# Menampilkan semua item yang telah dijual
warehouse.list_sold_items()
print()

# Menghapus item dari gudang
warehouse.remove_item("Smartphone")
print()

# Menampilkan semua item di gudang setelah penghapusan
warehouse.list_all_items()
print()

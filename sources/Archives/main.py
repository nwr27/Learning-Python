class Kendaraan:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def deskripsi(self):
        return f"{self.tahun} {self.merk} {self.model}"

    def suara(self):
        return "Vroom"


class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun, jumlah_pintu):
        super().__init__(merk, model, tahun)
        self.jumlah_pintu = jumlah_pintu

    def deskripsi(self):
        return f"{self.tahun} {self.merk} {self.model} dengan {self.jumlah_pintu} pintu"


class Motor(Kendaraan):
    def suara(self):
        return "Ngeeng"


mobil_saya = Mobil("Toyota", "Camry", 2020, 4)
motor_saya = Motor("Honda", "CBR", 2018)

print(mobil_saya.deskripsi())
print(mobil_saya.suara())
print(motor_saya.deskripsi())
print(motor_saya.suara())

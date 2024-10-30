class PersegiPanjang:
    def __init__(self, panjang, lebar):
        # Konstruktor untuk inisialisasi properti panjang dan lebar
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        # Fungsi untuk menghitung keliling persegi panjang
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        # Fungsi untuk menghitung luas persegi panjang
        return self.panjang * self.lebar

    def __str__(self):
        # Fungsi untuk mengembalikan representasi string dari objek
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    
    
# Membuat objek dari kelas PersegiPanjang
persegi_panjang = PersegiPanjang(10, 2)

# Menampilkan string objek
print(persegi_panjang)

# Menghitung keliling
print("Keliling:", persegi_panjang.keliling(), "cm")

# Menghitung luas
print("Luas:", persegi_panjang.luas(), "cm²")

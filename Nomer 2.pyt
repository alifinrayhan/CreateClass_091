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
    
    
def main() :
    try:
        panjang = float(input("Masukkan panjang persegi:  "))
        lebar = float(input("Masukkan lebar persegi: "))

        if(panjang <=0 or lebar <=0):
            print("Nilai tidak boleh negatif atau nol")
            return
        else:
            pp = PersegiPanjang(panjang, lebar)
            print(pp)
            print("keliling: ", pp.keliling())
            print("Luas", pp.luas())

    except ValueError:
        print("Input harus berupa angka.")

main()
        
        
# Program menghitung luas atau keliling trapesium (versi interaktif)
def hitung_luas():
    print("\n=== Hitung Luas Trapesium ===")
    a = float(input("Masukkan panjang sisi sejajar pertama (a): "))
    b = float(input("Masukkan panjang sisi sejajar kedua (b): "))
    t = float(input("Masukkan tinggi trapesium (t): "))

    luas = 0.5 * (a + b) * t
    print(f"Luas trapesium = {luas:.2f} cm\n")

def hitung_keliling():
    print("\n=== Hitung Keliling Trapesium ===")
    a = float(input("Masukkan panjang sisi sejajar pertama (a): "))
    b = float(input("Masukkan panjang sisi sejajar kedua (b): "))
    c = float(input("Masukkan panjang sisi miring pertama (c): "))
    d = float(input("Masukkan panjang sisi miring kedua (d): "))

    keliling = a + b + c + d
    print(f"Keliling trapesium = {keliling:.2f} cm\n")

# Program utama
while True:
    print("======= Program Menghitung Luas atau Keliling Trapesium =======")
    print("Pilih perhitungan yang ingin dilakukan:")
    print("1. Luas Trapesium")
    print("2. Keliling Trapesium")
    print("3. Keluar dari program")

    pilihan = input("Masukkan pilihan (1,2 atau 3): ")

    if pilihan == "1":
        hitung_luas()
    elif pilihan == "2":
        hitung_keliling()
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
        break
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.\n")

    lanjut = input("Apakah Anda ingin melakukan perhitungan lain? (Yes/No): ").lower()
    if lanjut != "yes" and lanjut != "y":
        print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
        break
    print() 

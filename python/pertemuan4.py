# # Program menghitung biaya parkir berdasarkan lama waktu

# # Input lama waktu parkir (dalam jam)
# lama_parkir = float(input("Masukkan lama parkir (jam): "))

# # Logika perhitungan biaya
# if lama_parkir <= 1:
#     biaya = 3000
# elif lama_parkir <= 3:
#     biaya = 5000
# else:
#     tambahan_jam = lama_parkir - 3
#     biaya = 5000 + (2000 * tambahan_jam)

# # Output hasil
# print(f"Biaya parkir adalah: Rp {int(biaya):,}")


# # Program menentukan kategori umur seseorang

# # Input umur
# umur = int(input("Masukkan umur: "))

# # Logika menentukan kategori
# if umur < 5:
#     kategori = "Balita"
# elif umur <= 12:
#     kategori = "Anak-anak"
# elif umur <= 17:
#     kategori = "Remaja"
# elif umur <= 59:
#     kategori = "Dewasa"
# else:
#     kategori = "Lansia"

# # Output hasil
# print(f"Kategori umur: {kategori}")



# # Program login sederhana
# # Data login yang benar
# username_benar = "admin"
# password_benar = "12345"

# # Input dari pengguna
# username = input("Masukkan username: ")
# password = input("Masukkan password: ")

# # Logika validasi login
# if username != username_benar:
#     print("Username salah")
# elif password != password_benar:
#     print("Password salah")
# else:
#     print("Login berhasil")


# Program mencari nilai terbesar dan terkecil dari a, b, c, d
# Input empat bilangan bulat
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
d = int(input("Masukkan nilai d: "))
# Inisialisasi awal
terbesar = a
terkecil = a
# Mencari nilai terbesar
if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d
# Mencari nilai terkecil
if b < terkecil:
    terkecil = b
if c < terkecil:
    terkecil = c
if d < terkecil:
    terkecil = d
# Output hasil
print(f"Nilai terbesar adalah: {terbesar}")
print(f"Nilai terkecil adalah: {terkecil}")

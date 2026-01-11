# # Soal 1
# angka = [10, 20, 10, 100, 20, 20, 3, 0, 10, 50, 10]
# print("=== Menampilkan List dengan Loop for ===")
# for i in angka:
#     print(i)
# # Soal 2
# print("\n=== Menghitung jumlah kemunculan angka ===")
# jumlah_10 = 0
# jumlah_20 = 0
# for i in angka:
#     if i == 10:
#         jumlah_10 += 1
#     elif i == 20:
#         jumlah_20 += 1
# print(f"Jumlah angka 10 ada: {jumlah_10}")
# print(f"Jumlah angka 20 ada: {jumlah_20}")
# # Soal 3
# print("\n=== Mencari Nilai Terbesar ===")
# terbesar = angka[0]  # anggap elemen pertama sebagai yang terbesar
# for i in angka:
#     if i > terbesar:
#         terbesar = i
# print(f"Nilai terbesar adalah: {terbesar}")
# # Soal 4
# print("\n===Mencari Nilai Terkecil===")
# terkecil = angka[0]
# for i in angka:
#     if i  <= terkecil:
#         terkecil = i
# print(f"\nNilai Tekecekil adalah: {terkecil}")



# Tugas
import random
import string
# Semua karakter yang akan disandikan (A-Z dan 0-9)
karakter = list(string.ascii_uppercase + string.digits)
# Simbol yang akan digunakan untuk mengganti (boleh ubah sesuai keinginan)
simbol = list("!@#$%^&*()_+-=[]{}|;:',.<>?/")
# Jika simbol kurang banyak, gandakan supaya cukup
while len(simbol) < len(karakter):
    simbol *= 2
random.shuffle(simbol)
# Buat kamus kunci
kunci = {}
for i, huruf in enumerate(karakter):
    kunci[huruf] = simbol[i]
# --- Tampilkan tabel kunci ---
print("=== Tabel Kunci Sandi ===")
for h in karakter:
    print(f"{h} → {kunci[h]}")
print("\n==========Silahkan Login============")
# --- Input password dari user ---
password = input("Masukkan password: ").upper()
# --- Proses enkripsi ---
tersandikan = ""
for huruf in password:
    if huruf in kunci:
        tersandikan += kunci[huruf]
    else:
        tersandikan += kunci["LAINYA"]
# --- Output hasil ---
print("Tersandikan :", tersandikan)
print("=========Terima Kasih=============")
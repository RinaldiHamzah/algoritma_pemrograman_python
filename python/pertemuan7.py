# def fibonacci_rekursif(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

# # Contoh penggunaan:
# for i in range(10):
#     print(fibonacci_rekursif(i), end=" ")


# Data KHS
khs = {
    1: {'kode': 'K20001', 'mata_kul': 'Pemrograman', 'nilai': 'A', 'sks': 3},
    2: {'kode': 'K20002', 'mata_kul': 'Jaringan komputer', 'nilai': 'B', 'sks': 3},
    3: {'kode': 'K20003', 'mata_kul': 'Algoritma', 'nilai': 'A', 'sks': 3},
    4: {'kode': 'K20004', 'mata_kul': 'Statistik', 'nilai': 'B', 'sks': 3},
    5: {'kode': 'K20005', 'mata_kul': 'Matematika', 'nilai': 'B', 'sks': 3},
    6: {'kode': 'K20006', 'mata_kul': 'Fisika', 'nilai': 'B', 'sks': 3}
}

# Fungsi untuk menghitung skor
def hitungSkor(nilai, sks):
    bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
    if nilai in bobot_nilai:
        return bobot_nilai[nilai] * sks
    else:
        return 0  

# Menampilkan hasil dalam format tabel
print("KODE\t\tMATAKULIAH\t\tNILAI\tSKS\tSKOR")
print("="*60)

for data in khs.values():
    kode = data['kode']
    mata_kul = data['mata_kul']
    nilai = data['nilai']
    sks = data['sks']
    skor = hitungSkor(nilai, sks)
    print(f"{kode}\t{mata_kul:20}\t{nilai}\t{sks}\t{skor}")

total = 0       # penjumlahan angka
count = 0       # jumlah input
nilai = 0     
while nilai >= 0:
    nilai = float(input("Masukkan nilai (negatif untuk berhenti): "))
    
    if nilai < 0:
        break 

    total += nilai
    count += 1

if count > 0:
    rata_rata = total / count
    print(f"Rata-rata nilai = {rata_rata:f}")
else:
    print("Tidak ada data nilai yang dimasukkan.")



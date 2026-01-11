def hitung_total():
    total = 0
    while True:
        nama = input("Masukkan nama barang: ")
        if nama.lower() == "selesai":
            break
        harga = int(input("Masukkan harga: "))
        total += harga
    return total

total_belanja = hitung_total()
print(f"Total belanja sebelum diskon: {total_belanja}")

if total_belanja > 100000: 
    diskon = total_belanja * 0.10
    total_bayar = total_belanja - diskon
    print("Diskon 10%")
else:
    total_bayar = total_belanja
print(f"Total bayar: {int(total_bayar)}")


def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y

def menu():
    print("Pilih Operasi")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")

def kalkulator():
    menu()
    pilih = input("Masukkan pilihan operasi (1/2/3/4): ")

    if pilih == "1":
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        print (bilangan1,"+",bilangan2, "=",tambah(bilangan1, bilangan2))
              
    elif pilih == "2":
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        print (bilangan1, "-", bilangan2, "=",kurang(bilangan1, bilangan2))     
               
    elif pilih == "3":
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        print (bilangan1, "*", bilangan2, "=",kali(bilangan1, bilangan2))

    elif pilih == "4":
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))
        print (bilangan1, "/", bilangan2, "=",bagi(bilangan1, bilangan2))

    else:
        print("Input salah")                    
kalkulator()
       

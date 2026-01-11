# def hitung(x, y):
#     if x == y:
#         print("Error: x dan y tidak boleh sama")
#         return None
#     else:
#         return ((x**2 + y**2) / (x - y))**3
# x = int(input("Masukkan x: "))
# y = int(input("Masukkan y: "))

# hasil = hitung(x, y)
# if hasil is not None:
#     print("Hasil =", hasil)

# b = [10, 20, 2, 0, 2, 1, 2, 100]
# N = len(b)

# for i in range(N - 1):
#     for j in range(N - 1):
#         if b[j] < b[j + 1]:
#             temp = b[j]
#             b[j] = b[j + 1]
#             b[j + 1] = temp
# print(b)

b = ["C", "B", "D", "X", "Q", "M", "A"]
N = len(b)

for i in range(N - 1):
    tukar = False
    for j in range(N - 1 - i):
        if b[j] > b[j + 1]:
            temp = b[j]
            b[j] = b[j + 1]
            b[j + 1] = temp
            tukar = True
    if not tukar:
        break
print(b)

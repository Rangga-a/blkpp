# index = [0, 1, 2, 3, 4, 5]
# nama = ["Ahmad", "Budi", "Cici", "Dedi", "Eka"]
# nilai = [80, 90, 75, 85, 95]

# nama_slice = nama[0:6]
# nilai_slice = nilai[0:6]

# nama_slice[2] = "Caca"
# nilai_slice[2] = 99


# print(nama_slice)
# print(nilai_slice)

# print(nama[0])
# print(nilai[1])

# print("\n")
# print(nama)
# print("\n")
# print(f"Nama: {nama[1]}, mendapatkan Nilai: {nilai[1]}")

# print("Panjang Data Nama: ", len(nama))

# for i in range(len(nama)):
#     print(f"Nama: {nama[i]}, mendapatkan Nilai: {nilai[i]}")


#------------------------------------------------------------------------

index = [0, 1, 2, 3, 4, 5, 6]
nama = ["Alice", "Bob", "Farah", "Edi", "Charlie", "Gita", "Hasti"]


nama_slice_3_tengah = nama[2:5]


print(nama_slice_3_tengah)  # ['Charlie', 'Edi', 'Farah']


nama_slice_3_tengah[2] = "Clara"
print("\n")
print(nama_slice_3_tengah)


# INSERT
nama_slice_3_tengah.insert(1, "Zara")
print("\n INSERT")
print(nama_slice_3_tengah)


# APPEND
nama_slice_3_tengah.append("Dina")
print("\n APPEND")
print(nama_slice_3_tengah)


# SORT
nama_slice_3_tengah.sort()
print("\n SORT")
print(nama_slice_3_tengah)

# POP
nama_slice_3_tengah.pop()
print("\n POP")
print(nama_slice_3_tengah)

#REVERSE
nama_slice_3_tengah.reverse()
print("\n REVERSE")
print(nama_slice_3_tengah)


# Print dengan index
# print("\n")


# print("Print dengan index")
# print(f"indeks -1 adalaha {nama[-1]}")
# print(f"panjang data dari nama = {len(nama)}")


# print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")


# for z in range(len(nama)):
#     print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")

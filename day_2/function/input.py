import aritmatika as a

# print("Hasil Penjumlahan: ", a.add(10, 5))
# print("Hasil Pengurangan: ", a.subtract(10, 5))
# print("Hasil Perkalian: ", a.multiply(10, 5))
# print("Hasil Pembagian: ", a.divide(10, 5))



berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (cm): "))

hasil_bmi = a.bmi(berat, tinggi)

a.kategori_bmi(hasil_bmi)

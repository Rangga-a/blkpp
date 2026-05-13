berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (cm): "))

bmi = berat / ((tinggi / 100) ** 2)
# bmi = berat / (tinggi * tinggi)

print(f"BMI Anda adalah: {bmi:.2f}")
if bmi < 18.5:
    print("Anda termasuk kategori: Underweight")
elif bmi < 25:
    print("Anda termasuk kategori: Normal weight")  
elif bmi < 30:
    print("Anda termasuk kategori: Overweight")
else:
    print("Anda termasuk kategori: Obesity")    
    

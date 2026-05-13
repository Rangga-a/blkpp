def add(a = None,b = None):
    if a is None or b is None:
        return "Error: Kedua parameter harus diisi."
    total = a + b
    return total

def subtract(a = None,b = None):
    if a is None or b is None:
        return "Error: Kedua parameter harus diisi."
    total = a - b
    return total

def multiply(a = None,b = None):
    if a is None or b is None:
        return "Error: Kedua parameter harus diisi."
    total = a * b
    return total

def divide(a = None,b = None):
    if a is None or b is None:
        return "Error: Kedua parameter harus diisi."
    if b == 0:
        return "Error: Tidak bisa dibagi oleh nol."
    total = a / b
    return total



def bmi(berat, tinggi):
    tinggi_m = tinggi / 100
    return berat / (tinggi_m ** 2)

def kategori_bmi(bmi):
    print(f"BMI Anda adalah: {bmi:.2f}")
    if bmi < 18.5:
        print("Anda termasuk kategori: Underweight")
    elif bmi < 25:
        print("Anda termasuk kategori: Normal weight")
    elif bmi < 30:
        print("Anda termasuk kategori: Overweight")         
    else:
        print("Anda termasuk kategori: Obesity")



# print(f" Hasil dari penjumlahan: {add()}")
# print(f" Hasil dari pengurangan: {subtract(10, 5)}")
# print(f" Hasil dari perkalian: {multiply()}")
# print(f" Hasil dari pembagian: {divide()}")

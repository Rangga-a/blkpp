# from datetime import datetime

# def sapa():
#     print("Halo, selamat siang")
    
# def sapa_nama(nama=None):
#     if nama is None:
#         print("Halo, selamat datang di kelas Data Analyst!")
#     else:
#         print(f"Halo {nama}, selamat datang di kelas Data Analyst!")
    
# # def sapa_nama_alamat(nama, alamat):
# #     print(f"Halo {nama}, selamat datang di kelas Data Analyst!  Aku Berasal dari {alamat}.")   
    

# sapa()
# sapa_nama("")
# # sapa_nama_alamat("Rangga", "Jogja")
# print(datetime.now())


#------------------------------------------------------------------------


def sapa():
   print("HELLO HAI")

def sapa_nama(nama=None):
   if nama is None:
       print("Silakan masukkan nama")
       return

   print(f"HELLO {nama}")

# print("Sebelum memanggil fungsi")
sapa()
sapa_nama("Rangga")
sapa_nama()
# print(datetime.now())

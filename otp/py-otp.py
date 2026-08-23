"""
Project validasi OTP / One Time Password
"""
import time as memek
import random as kontol
import os


def bersihin():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Await...")

memek.sleep(3)
secure = kontol.randint(1000, 8888)
print(f"OTP: {secure}")

memek.sleep(2)
bersihin()
masuk_otp = int(input("Masukan OTP 4 digit sebelum nya\n: "))

if masuk_otp == secure:
	print("Berhasil!")
else:
	print("Kontol Mati aja ku hekur anjing")

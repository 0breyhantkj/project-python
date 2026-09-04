import random

nomor = random.randint(1,100)
tebakan = 0

while tebakan != nomor:
	tebakan = int(input("Masukan angka tebakan 1-100: "))
	if (tebakan < nomor):
		print(f"Angka {tebakan}, terlalu rendah 🔻")
	elif ( tebakan > nomor):
		print(f"Angka {tebakan}, terlalu besar 🔺️")
	else:
		print(f"Selamat anda benar jawaban nya: {tebakan}\nBtw reyhan ganteng banget WOKK🥰😍😍🤩")

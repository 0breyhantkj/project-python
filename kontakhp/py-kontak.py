"""Project Dictionary, Kontak python"""

kontak = {
	"biden": "85777",
	"jesen": "716255262",
	"kepinz": "98282727",
	"kepinj": "87262727",
	"paris": "02828282",
	"reyhan": "928727262",
	"ibnu": "99999"
}

while True:
	print(f"""
1. Lihat kontak
2. Tambah kontak
3. Hapus kontak
4. Keluar""")

	menu = input("Masukan [1-3] : ")
	if menu == "1":
		for nama, nomor in kontak.items():
			print(f"{nama}: {nomor}")
	elif menu == "2":
		add_nama = input("Masukan nama: ")
		add_nomor = input("Masukan nomor: ")
		kontak[add_nama] = add_nomor
		for nama, nomor in kontak.items():
			print(f"{nama}: {nomor}")
	elif menu == "3":
		hapus = int(input("Masukan angka: "))
		nama = list(kontak)[hapus - 1]
		del kontak[nama]
		for nama, nomor in kontak.items():
			print(f"{nama}: {nomor}")
	elif menu == "4":
		break
	else:
		print("Tidak ada aksi")

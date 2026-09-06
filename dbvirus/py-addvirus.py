""" Project saved memory | Database Malware saya """

print(f"""
{"-"*10}

Script ini menyimpan input ke dalam memory, dengan nama variabel list_malware, lalu akan di tampilkan ulang ke dalam loop

{"-"*10}
""")


list_malware = []

while True:
	nama = input("Masukan nama: ")
	pencipta = input("Siapa pembuat nya: ")
	
	malware_baru = [nama,pencipta]
	list_malware.append(malware_baru)
	
	for index,malware in enumerate(list_malware):
		print(f"\n{index+1} | {malware[0]} | {malware[1]} ")
		

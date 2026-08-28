#variabel
sisi = 9

#==========[ Persegi Panjang ]==========#
jumlah = 1
while True:
	print("*"*19)
	jumlah +=1
	
	if jumlah > 5:
		break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("\n")
#==========[ Persegi ]==========#
jumlah = 1
while True:
	print("*"*10)
	jumlah +=1
	
	if jumlah > 5:
		break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print("\n\n")
#==========[ Segitiga siku-siku ]==========#
jumlah = 1
while True:
	print("*"*jumlah)
	jumlah += 1

	if jumlah > sisi:
		break
print("END")
#versi 2
jumlah = 1
while True:
	if (jumlah%2):
		print("*"*jumlah)
		jumlah += 1
	else:
		jumlah += 1
		continue
	if jumlah > sisi:
		break
print("END")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#==========[ Segitiga siku-siku kebalik ] ==========#
jumlahv2 = sisi
while True:
	print("*"*jumlahv2)
	jumlahv2 -= 1

	if jumlahv2 < 1:
		break
print("END")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#==========[ Segitiga sama kaki ] ==========#
jumlah = 1
while True:
	if (jumlah%2):
		spasi = (sisi - jumlah) // 2
		print(" "*spasi + "*"*jumlah)
		jumlah += 1
	else:
		jumlah += 1
		continue
	if jumlah > sisi:
		break
print("END")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#==========[ Piramid Flip ]==========#
jumlahv2 = sisi
while True:
	spasi = (sisi - jumlahv2) // 2
	print(" "*spasi + "*"*jumlahv2)
	jumlahv2 -= 2

	if jumlahv2 < 1:
		break
print("END")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

jumlah = 1
jumlahv2 = sisi
naik = True

while True:
	spasi = (sisi - jumlah) // 2
	print(" "*spasi + "*"*jumlah)
	if naik:
		jumlah += 2
	
		if jumlah > sisi:
			jumlah -= 4
			naik = False
	
	else:
		jumlah -= 2
		
		if jumlah < 1:
			break
print("END")

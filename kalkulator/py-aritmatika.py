"""
Kalkulator sederhana, dan hitungan ARITMATIKA + - * // %
"""

print(f"""
    {5*"="+"KALKULATOR SEDERHANA"+5*"="}

1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Modulus
""")

aksi_menu = input("Masukan pilihan [1-5]: ")

def penjumlahan():
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input(f"{angka1} di tambah dengan angka: "))
    proses = angka1 + angka2
    print("Hasil nya adalah: ", proses)

def pengurangan():
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input(f"{angka1} di kurang dengan angka: "))
    proses = angka1 - angka2
    print("Hasil nya adalah: ", proses)

def perkalian():
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input(f"{angka1} di kali dengan angka: "))
    proses = angka1 * angka2
    print("Hasil nya adalah: ", proses)
    

def pembagian():
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input(f"{angka1} di bagi dengan angka: "))
    proses = angka1 // angka2
    print("Hasil nya adalah: ", proses)
    

def modulus():
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input(f"{angka1} di modulus dengan angka: "))
    proses = angka1 % angka2
    print("Hasil nya adalah: ", proses)


if aksi_menu == "1":
    penjumlahan()
elif aksi_menu == "2" :
    pengurangan()
elif aksi_menu == "3" :
    perkalian()
elif aksi_menu == "4" :
    pembagian()
elif aksi_menu == "5" :
    modulus()

else:
    print("Tidak ada aksi!")

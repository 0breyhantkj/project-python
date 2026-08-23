"""
Project sederhana converter nomor system

Encode & Decode

"""

print(f"""
    {5*"="+"CONVERTER NUMBER SYSTEM"+5*"="}
  [Decimal to NumberSys ]
1. Number to Binary
2. Number to Octal
3. Number to Hexadecimal

    
    [ NunberSys to Decimal ]
4. Binary to Number
5. Octal to Number
6. Hexadecimal to Number
""")

aksi_menu = input("Masukan pilihan [1-4]: ")

if aksi_menu == "1":
    binary = int(input("Masukan Nomor: "))
    print(f"Hasil:\n{bin(binary)}")
elif aksi_menu == "2":
    octal = int(input("Masukan Nomor: "))
    print(f"Hasil:\n{oct(octal)}")
elif aksi_menu == "3":
    hexadecimal = int(input("Masukan Nomor: "))
    print(f"Hasil:\n{hex(hexadecimal)}")
# Decode number system
elif aksi_menu == "4":
    binary = input("Masukan Nomor Biner: ")
    print(f"Hasil:\n{int(binary, 2)}")
elif aksi_menu == "5":
    octal = input("Masukan Nomor Oktal: ")
    print(f"Hasil:\n{int(octal, 8)}")
elif aksi_menu == "6":
    hexadecimal = input("Masukan Nomor Hexadecimal: ")
    print(f"Hasil:\n{int(hexadecimal, 16)}")
else:
    print("Tidak ada aksi!")

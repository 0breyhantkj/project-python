"""Keranjang Online sederhana"""

harga_kopi = 10000
harga_mie = 2500
harga_baju = 60000
harga_celana = 150000

memory = []

dompet = float(input("Masukan dompet hayalan anda: "))

while True:
    uang = f"{dompet:,.0f}".replace(",", ".")

    print(f"""
DOMPET: Rp{uang}

1. Harga kopi   : Rp{harga_kopi:,}
2. Harga mie    : Rp{harga_mie:,}
3. Harga baju   : Rp{harga_baju:,}
4. Harga celana : Rp{harga_celana:,}
""")

    belanja = int(input("Pilih angka 1-4 untuk memasukan ke keranjang: "))

    if belanja == 1:
        if dompet >= harga_kopi:
            memory.append(("Kopi", harga_kopi))
            dompet -= harga_kopi
        else:
            print("Uwang tidak cukup!")

    elif belanja == 2:
        if dompet >= harga_mie:
            memory.append(("Mie", harga_mie))
            dompet -= harga_mie
        else:
            print("Uwang tidak cukup!")

    elif belanja == 3:
        if dompet >= harga_baju:
            memory.append(("Baju", harga_baju))
            dompet -= harga_baju
        else:
            print("Uwang tidak cukup!")

    elif belanja == 4:
        if dompet >= harga_celana:
            memory.append(("Celana", harga_celana))
            dompet -= harga_celana
        else:
            print("Uwang tidak cukup!")

    else:
        print("Pilihan tidak valid!")
        break

    print("\nKERANJANG:")

    for nama, harga in memory:
        print(f"- {nama}: Rp{harga:,}")

    print()

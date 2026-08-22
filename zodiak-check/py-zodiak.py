import datetime as wektu

print(f"""Ramalan umur anda
""")

tanggal = int(input("Masukan tanggal: "))
bulan = int(input("Masukan bulan lahir: "))
tahun = int(input("Masukan Tahun lahir: "))
tanggal_lahir = wektu.date(tahun, bulan, tanggal)

# Tahun
tahun_ini = wektu.date.today().year
tot_year = tahun_ini - tanggal_lahir.year

# Bulan
bulan_ini = wektu.date.today().month
tot_month = (
    (tahun_ini - tanggal_lahir.year) * 12
    + (bulan_ini - tanggal_lahir.month)
)

# Hari
hari_ini = wektu.date.today()
tot_day = (hari_ini - tanggal_lahir).days

# Zodiak
bulan = tanggal_lahir.month
bulan = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
]
zodiak_bulan = [
    ["Januari", "Capricorn/Aquarius"],
    ["Februari", "Aquarius/Pisces"],
    ["Maret", "Pisces/Aries"],
    ["April", "Aries/Taurus"],
    ["Mei", "Taurus/Gemini"],
    ["Juni", "Gemini/Cancer"],
    ["Juli", "Cancer/Leo"],
    ["Agustus", "Leo/Virgo"],
    ["September", "Virgo/Libra"],
    ["Oktober", "Libra/Scorpio"],
    ["November", "Scorpio/Sagittarius"],
    ["Desember", "Sagittarius/Capricorn"]
]
data = zodiak_bulan[tanggal_lahir.month - 1]

print(f"""
Hari: {tanggal_lahir}
Hari: {tanggal_lahir:%A}
umur anda adalah: {tot_year} tahun
total bulan: {tot_month} dari bulan ini
total hari: {tot_day}

zidiak anda adalah: {data[1]}
""")

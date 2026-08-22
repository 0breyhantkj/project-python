"""
Latihan perulangan / lopping
for <variabel> in <jumlah>:
    <aksi>
<END>
"""
# Menu
print(f"""
    {5*"="+"PERULANGAN"+5*"="}
1. Perulangan String
2. Perulangan Range
3. Perulangan List
4. Perulangan Dictionary
""")
input_menu = str(input("Masukan pilihan [1-4]: "))

# Fungsi Loop String
def loop_string():
    text = input("Masukan text anda: ")
    for loop in text:
        print(loop)
    print("\nEND")


# Fungsi loop range
def loop_range():
    text = input("Masukan text anda: ")
    count = int(input("Masukan jumlah perulangan: "))

    for loop in range(count):
        print(text)
    print("\nEND")
    

# Fungsi loop list
def loop_list():
    text = input("Masukan text anda: ")
    count = input("Masukan list dengan koma [1,2.xx]: ")
    my_list = count.split(",")
    for loop in my_list:
        print(f"{loop} -> {text}")
    print("\nEND")


# Fungsi loop Directionary
def loop_dictionary():
    data = {
        "Nama": input("Masukkan nama mu: "),
        "Umur": input("Masukkan umur mu: ")
    }
    count = int(input("Jumlah perulangan: "))
    for loop in range(count):
        print(data)
    print("\nEND")

# Fungsi if / pemilihan
if input_menu == "1":
    loop_string()
elif input_menu == "2":
    loop_range()
elif input_menu == "3":
    loop_list()
elif input_menu == "4":
    loop_dictionary()
else:
    print("Tiada Aksi!")

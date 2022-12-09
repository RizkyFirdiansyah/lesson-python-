def header():
    print("=" * 45)
    print("Latihan Function Calculator")
    print("=" * 45)   
    
def input_user():
    angka1 = int(input("Masukkan Angka Pertama :"))
    angka2 = int(input("Masukkan Angka Kedua :"))
    return angka1,angka2

def penjumlahan(angka1,angka2):

    return angka1 + angka2

def pengurangan(angka1,angka2):
    return angka1 - angka2

def perkalian(angka1,angka2):
    return angka1 * angka2

def pembagian(angka1,angka2):
    return angka1 / angka2

def display(message,value):
    print(f"Hasil Perhitungan {message} = {value}")

while True:
    header()
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    opsi = input("Pilih Operasi Perhitungan : ")

    if opsi == "1":
        PENJUMLAHAN = penjumlahan(ANGKA1,ANGKA2)
        display("Penjumlahan", PENJUMLAHAN)

    if opsi == "2":
        PENGURANGAN = pengurangan(ANGKA1,ANGKA2)
        display("Pengurangan", PENGURANGAN)
    
    if opsi == "3":
        PERKALIAN = perkalian(ANGKA1,ANGKA2)
        display("Perkalian", PERKALIAN)

    if opsi == "4":
        PEMBAGIAN = pembagian(ANGKA1,ANGKA2)
        display("Pembagian", PEMBAGIAN)
    
    else:
        print("Maaf, Menu Yang Anda Pilih Tidak Tersedia")
        break
    ANGKA1,ANGKA2 = input_user()

    isContinue = input("Apakah Lanjut (y/n)")
    if isContinue == "n" :
        break
print("Program Selesai Thank's")



from os import system

def clear():
	system('clear')
clear()

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

    ANGKA1,ANGKA2 = input_user()

    if opsi == "1":
        PENJUMLAHAN = penjumlahan(ANGKA1,ANGKA2)
        display("Penjumlahan", PENJUMLAHAN)

    elif opsi == "2":
        PENGURANGAN = pengurangan(ANGKA1,ANGKA2)
        display("Pengurangan", PENGURANGAN)
    
    elif opsi == "3":
        PERKALIAN = perkalian(ANGKA1,ANGKA2)
        display("Perkalian", PERKALIAN)

    elif opsi == "4":
        PEMBAGIAN = pembagian(ANGKA1,ANGKA2)
        display("Pembagian", PEMBAGIAN)
    
    else:
        print("Maaf, Menu Yang Anda Pilih Tidak Tersedia")
      

    isContinue = input("Apakah Lanjut (y/n)")
    clear()
    if isContinue == "n" :
        break
print("Program Selesai Thank's")



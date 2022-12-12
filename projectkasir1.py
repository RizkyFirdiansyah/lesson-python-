import datetime


print("=" * 45)
print("========== SELAMAT DATANG di KOPIKU =========")
print("<------------------------------------------->")
print("================ DAFTAR MENU ================")
print("=" * 45)
print("1. Lihat Member")
print("2. Tambah Member")
print("3. Lihat Daftar Menu")
print("4. Kasir")
print("5. Keluar")
opsi = input("Pilih Menu :")

menu = [
    {"jenis_menu":"makanan", "nama_menu":"Mie Kobong", "Harga":15.000},
    {"jenis_menu":"makanan", "nama_menu":"Nasi Goreng", "Harga":17.000},
    {"jenis_menu":"makanan", "nama_menu":"Tempe Geprek", "Harga":13.000},
    {"jenis_menu":"makanan", "nama_menu":"Ayam Tusuk", "Harga":18.000},
    {"jenis_menu":"makanan", "nama_menu":"Bakso", "Harga":20.000},
    {"jenis_menu":"minuman", "nama_menu":"Kopi Latte", "Harga":11.000},
    {"jenis_menu":"minuman", "nama_menu":"Expresso", "Harga":10.000},
    {"jenis_menu":"minuman", "nama_menu":"Cappucino", "Harga":13.000},
    {"jenis_menu":"minuman", "nama_menu":"Red Velvet", "Harga":12.000},
    {"jenis_menu":"minuman", "nama_menu":"Lemon Tea", "Harga":10.000}
]

member = [
    {"id":"A000Z", "nama_member":"Feri", "tgl_join":"10-10-2022"},
    {"id":"A001Z", "nama_member":"Zaidan", "tgl_join":"20-10-2022"},
    {"id":"A002Z", "nama_member":"Ani", "tgl_join":"29-10-2022"},
    {"id":"A003Z", "nama_member":"Dany", "tgl_join":"1-11-2022"},
    {"id":"A004Z", "nama_member":"Robert", "tgl_join":"10-11-2022"}
]

# Function
def lihat_member():
    i = 0
    no = 1
    print("=============== DAFTAR MEMBER ===============")
    while i < len(member):
        print(f'{no}, {member[i]["id"]}, nama : {member[i]["nama_member"]}, sejak {member[i]["tgl_join"]}')
        no += 1
        i += 1

def lihat_menu(jenis):
    i = 0
    no = 1
    if(jenis=="minuman"):
        print("============ DAFTAR MENU MINUMAN ============")
        while i < len(menu):
            if(menu[i] ["jenis_menu"]==jenis):
                print(f'{no}. {menu[i]["nama_menu"]}, Harga : {menu[i]["Harga"]}')
                no += 1
            i += 1
    if(jenis=="makanan"):
        print("============ DAFTAR MENU MAKANAN ============")
        while i < len(menu):
            if(menu[i] ["jenis_menu"]==jenis):
                print(f'{no}. {menu[i]["nama_menu"]}, Harga : {menu[i]["Harga"]}')
                no += 1
            i += 1

if opsi == "1":
    lihat_member()

if opsi == "3":
    lihat_menu("minuman")
    lihat_menu("makanan")
    






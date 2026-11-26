from kalender import tampilkan_bulan
from form_acara import input_acara

def menu():
    while True:
        print("\n=== SICANA ===")
        print("1. Lihat kalender")
        print("2. Tambah acara")
        print("0. Keluar")
        pilih = input("Pilih: ")
        if pilih == "1":
            tahun = int(input("Tahun: "))
            bulan = int(input("Bulan: "))
            tampilkan_bulan(tahun, bulan)
        elif pilih == "2":
            input_acara()
        elif pilih == "0":
            break

if __name__ == "__main__":
    menu()

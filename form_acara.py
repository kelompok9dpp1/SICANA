from datetime import datetime
from database import tambah_jadwal, ubah_jadwal

HARI_VALID = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

def input_hari():
    while True:
        hari = input("Hari (Senin-Sabtu): ").strip().capitalize()
        if hari in HARI_VALID:
            return hari
        print("Hari tidak valid, coba lagi.")

def input_jam():
    while True:
        jam = input("Jam mulai (HH:MM): ").strip()
        try:
            datetime.strptime(jam, "%H:%M")
            return jam
        except ValueError:
            print("Format jam salah, contoh: 08:00")

def input_teks(label):
    while True:
        teks = input(f"{label}: ").strip()
        if teks:
            return teks
        print(f"{label} tidak boleh kosong.")

def input_jadwal():
    print("\n=== Tambah Jadwal Matkul ===")
    hari = input_hari()
    jam = input_jam()
    matkul = input_teks("Nama matkul")
    ruang = input_teks("Ruang")
    tambah_jadwal(hari, jam, matkul, ruang)
    print(f"Jadwal {matkul} hari {hari} jam {jam} disimpan.")

def edit_jadwal():
    print("\n=== Edit Jadwal Matkul ===")
    id_jadwal = input_teks("ID jadwal yang mau diedit")
    hari = input_hari()
    jam = input_jam()
    matkul = input_teks("Nama matkul")
    ruang = input_teks("Ruang")
    ubah_jadwal(id_jadwal, hari, jam, matkul, ruang)
    print("Jadwal berhasil diubah.")

# Form tambah/edit acara. Dikerjakan Anggota 3.
from database import tambah_acara

def input_acara():
    judul = input("Judul acara: ")
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    jam = input("Jam (HH:MM): ")
    tambah_acara(judul, tanggal, jam)
    print("Acara disimpan.")

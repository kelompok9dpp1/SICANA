# Tampilan kalender + jadwal matkul. Dikerjakan Anggota 2.
import calendar
import datetime

try:
    from database import ambil_jadwal
except ImportError:
    # Data contoh sementara, sampai S selesai bikin ambil_jadwal
    def ambil_jadwal(hari):
        contoh = {
            "Senin": [{"jam": "08:00", "matkul": "DDP1", "ruang": "A101"}],
            "Rabu": [{"jam": "10:00", "matkul": "Matdis", "ruang": "B202"}],
        }
        return contoh.get(hari, [])

NAMA_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

def tampilkan_bulan(tahun, bulan):
    print(calendar.month(tahun, bulan))

def tampilkan_jadwal_tanggal(tahun, bulan, tanggal):
    hari = NAMA_HARI[datetime.date(tahun, bulan, tanggal).weekday()]
    jadwal = ambil_jadwal(hari)
    print(f"Jadwal {hari}, {tanggal}-{bulan}-{tahun}:")
    if not jadwal:
        print("  Tidak ada kuliah")
    for m in jadwal:
        print(f"  {m['jam']}  {m['matkul']}  ({m['ruang']})")

def tampilkan_jadwal_mingguan():
    print("\n=== Jadwal Minggu Ini ===")
    for hari in NAMA_HARI[:6]:
        print(f"\n{hari}")
        jadwal = sorted(ambil_jadwal(hari), key=lambda m: m["jam"])
        if not jadwal:
            print("  -")
        for m in jadwal:
            print(f"  {m['jam']}  {m['matkul']}  ({m['ruang']})")

def tampilkan_jadwal_hari_ini():
    hari_ini = datetime.date.today()
    tampilkan_jadwal_tanggal(hari_ini.year, hari_ini.month, hari_ini.day)

if __name__ == "__main__":
    tampilkan_jadwal_mingguan()
    tampilkan_jadwal_hari_ini()
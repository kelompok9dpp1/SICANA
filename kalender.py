# Logika kalender SICANA. Dikerjakan Anggota 2.
# Fungsi di sini MENGEMBALIKAN data, tidak print, supaya bisa dipakai di web.
import datetime

try:
    from database import ambil_jadwal
except ImportError:
    def ambil_jadwal(hari):
        contoh = {
            "Senin": [{"jam": "08:00", "matkul": "DDP1", "ruang": "A101"}],
            "Rabu": [{"jam": "10:00", "matkul": "Matdis", "ruang": "B202"}],
        }
        return contoh.get(hari, [])

NAMA_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

CONTOH_DEADLINE = [
    {"tanggal": "2026-12-03", "judul": "Laporan DDP1", "jenis": "Tugas"},
    {"tanggal": "2026-12-15", "judul": "UAS Matdis", "jenis": "Ujian"},
]

def nama_hari(tanggal):
    return NAMA_HARI[tanggal.weekday()]

def jadwal_tanggal(tanggal):
    hari = nama_hari(tanggal)
    jadwal = sorted(ambil_jadwal(hari), key=lambda m: m["jam"])
    return {"tanggal": tanggal, "hari": hari, "jadwal": jadwal}

def jadwal_mingguan():
    return {hari: sorted(ambil_jadwal(hari), key=lambda m: m["jam"])
            for hari in NAMA_HARI[:6]}

def deadline_terdekat(jumlah_hari=7, hari_ini=None):
    hari_ini = hari_ini or datetime.date.today()
    hasil = []
    for d in CONTOH_DEADLINE:
        tgl = datetime.date.fromisoformat(d["tanggal"])
        sisa = (tgl - hari_ini).days
        if 0 <= sisa <= jumlah_hari:
            hasil.append({**d, "sisa": sisa})
    return sorted(hasil, key=lambda d: d["sisa"])

# Hanya untuk tes di terminal
if __name__ == "__main__":
    hari_ini = jadwal_tanggal(datetime.date.today())
    print(f"Jadwal {hari_ini['hari']}:", hari_ini["jadwal"] or "Tidak ada kuliah")
    for hari, jadwal in jadwal_mingguan().items():
        print(hari, jadwal)
    for d in deadline_terdekat(30):
        print(f"[{d['jenis']}] {d['judul']}, {d['sisa']} hari lagi")
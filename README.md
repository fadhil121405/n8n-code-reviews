def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0  # Menghindari ZeroDivisionError jika list kosong
    return sum(daftar_nilai) / len(daftar_nilai)

def cari_nilai_max(data):
    if not data:
        return None  # Menghindari IndexError jika list kosong
    return max(data)  # Menggunakan fungsi bawaan Python yang lebih cepat dan menghindari shadowing

def bagi(a, b):
    if b == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
        return None
    return a / b

# Eksekusi dengan data pengujian
nilai = [80, 90, 100, 70, 85]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Nilai tertinggi:", cari_nilai_max(nilai))

# Penanganan kasus pembagian dengan nol
hasil_bagi = bagi(10, 0)
if hasil_bagi is not None:
    print("Hasil bagi:", hasil_bagi)

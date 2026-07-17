def hitung_rata_rata(daftar_nilai):
    if not daftar_nilai:
        return 0  
    return sum(daftar_nilai) / len(daftar_nilai)

def cari_nilai_max(data):
    if not data:
        return None  
    
    nilai_tertinggi = data[0]
    for x in data:
        if x > nilai_tertinggi:
            nilai_tertinggi = x
    return nilai_tertinggi

def bagi(a, b):
    if b == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
        return None
    return a / b

nilai = [80, 90, 100, 70, 85]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Nilai tertinggi:", cari_nilai_max(nilai))

hasil_bagi = bagi(10, 0)
if hasil_bagi is not None:
    print("Hasil bagi:", hasil_bagi)
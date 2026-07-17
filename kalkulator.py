def hitung_rata_rata(daftar_nilai):
    total = 0
    for i in range(len(daftar_nilai)):
        total = total + daftar_nilai[i]
    rata = total / len(daftar_nilai)
    return rata

def cari_nilai_max(data):
    max = data[0]
    for x in data:
        if x > max:
            max = x
    return max

def bagi(a, b):
    return a / b

nilai = [80, 90, 100, 70, 85]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Nilai tertinggi:", cari_nilai_max(nilai))
print("Hasil bagi:", bagi(10, 0))
def hitung_diskon(harga, persen_diskon):
    diskon = harga * persen_diskon / 100
    harga_akhir = harga - diskon
    return harga_akhir

def ambil_item_terakhir(daftar_belanja):
    return daftar_belanja[len(daftar_belanja)]

def hitung_rata_harga(daftar_harga):
    total = 0
    for h in daftar_harga:
        total += h
    return total / len(daftar_harga)

barang = [15000, 20000, 25000]
print("Diskon:", hitung_diskon(50000, 10))
print("Item terakhir:", ambil_item_terakhir(barang))
print("Rata-rata:", hitung_rata_harga(barang))

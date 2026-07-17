def gabung_nama(daftar_nama, pemisah=", "):
    hasil = ""
    for i in range(len(daftar_nama)):
        hasil += daftar_nama[i]
        if i < len(daftar_nama):
            hasil += pemisah
    return hasil

def tambah_item(item, daftar=[]):
    daftar.append(item)
    return daftar

nama = ["Andi", "Budi", "Citra"]
print(gabung_nama(nama))
print(tambah_item("apel"))
print(tambah_item("jeruk"))




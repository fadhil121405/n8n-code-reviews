class RekeningBank:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal
    
    def tarik(self, jumlah):
        self.saldo -= jumlah
        return self.saldo
    
    def transfer(self, rekening_tujuan, jumlah):
        self.tarik(jumlah)
        rekening_tujuan.saldo += jumlah

rek1 = RekeningBank(100000)
rek2 = RekeningBank(50000)
rek1.transfer(rek2, 200000)
print("Saldo rek1:", rek1.saldo)
print("Saldo rek2:", rek2.saldo)




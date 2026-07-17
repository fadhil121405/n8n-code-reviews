"""
bug3_bank_account.py
Simulasi sederhana kelas BankAccount.
File ini SENGAJA mengandung bug untuk keperluan testing AI agent.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah deposit harus positif")
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")
        # BUG: fungsi tidak return apa-apa padahal dipakai sebagai chaining di main()
        # (bukan bug fatal, tapi menyebabkan AttributeError saat dipakai chaining)

    def withdraw(self, amount):
        # BUG: tidak ada validasi saldo cukup atau tidak,
        # sehingga saldo bisa jadi minus tanpa batas
        self.balance -= amount
        self.history.append(f"Withdraw: -{amount}")

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        # BUG: seharusnya other_account.deposit(amount), 
        # tapi malah manggil deposit ke diri sendiri lagi (duplikasi dana hilang)
        self.deposit(amount)

    def apply_interest(self, rate_percent):
        # BUG: rate_percent dianggap sudah desimal (0.05),
        # padahal dipanggil dengan nilai persen (5 untuk 5%),
        # sehingga bunga yang ditambahkan jadi 100x lebih besar dari seharusnya
        interest = self.balance * rate_percent
        self.balance += interest
        self.history.append(f"Interest: +{interest}")

    def get_average_transaction(self):
        amounts = []
        for entry in self.history:
            # BUG: split(":")[1] masih mengandung tanda +/- dan spasi,
            # int() akan error saat mencoba parsing
            amounts.append(int(entry.split(":")[1]))
        return sum(amounts) / len(amounts)


if __name__ == "__main__":
    acc1 = BankAccount("Budi", 100000)
    acc2 = BankAccount("Siti", 50000)

    acc1.deposit(20000)
    acc1.withdraw(500000)  # seharusnya gagal karena saldo tidak cukup
    print("Saldo Budi setelah withdraw besar:", acc1.balance)

    acc1.transfer(acc2, 10000)
    print("Saldo Budi setelah transfer:", acc1.balance)
    print("Saldo Siti setelah menerima transfer:", acc2.balance)  # seharusnya bertambah, tapi tidak

    acc1.apply_interest(5)  # maksudnya 5%, tapi hasilnya salah karena bug rate
    print("Saldo Budi setelah bunga:", acc1.balance)

    try:
        print("Rata-rata transaksi:", acc1.get_average_transaction())
    except ValueError as e:
        print("Error di get_average_transaction:", e)

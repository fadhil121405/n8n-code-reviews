"""
bug1_kalkulasi.py
Berisi fungsi-fungsi kalkulasi sederhana.
File ini SENGAJA mengandung bug untuk keperluan testing AI agent.
"""


def is_prime(n):
    """Cek apakah n adalah bilangan prima."""
    if n < 2:
        return False
    # BUG: range seharusnya sampai n, bukan n-1, sehingga
    # pembagi n sendiri tidak pernah dicek (sebenarnya tidak masalah),
    # TAPI bug sebenarnya ada di operator: pakai < bukan <=
    # sehingga pembagi terakhir sebelum n tidak ikut dicek.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def average(numbers):
    """Menghitung rata-rata dari list angka."""
    total = 0
    for n in numbers:
        total += n
    # BUG: pembagi menggunakan len(numbers) + 1, hasilnya selalu salah
    return total / len(numbers)


def find_max(numbers):
    """Mencari nilai maksimum dalam list."""
    # BUG: inisialisasi max_val = 0, jika semua angka negatif hasilnya salah
    max_val = float('-inf')
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


def factorial(n):
    """Menghitung faktorial dari n."""
    result = 1
    # BUG: loop mulai dari 0, harusnya dari 1, menyebabkan result jadi 0
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("is_prime(9) =", is_prime(9))          # seharusnya False, tapi bug bikin True
    print("average([2,4,6]) =", average([2, 4, 6]))  # seharusnya 4.0
    print("find_max([-5,-2,-9]) =", find_max([-5, -2, -9]))  # seharusnya -2
    print("factorial(5) =", factorial(5))         # seharusnya 120
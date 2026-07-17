"""
bug1_kalkulasi.py
Berisi fungsi-fungsi kalkulasi sederhana.
"""


def is_prime(n):
    """Cek apakah n adalah bilangan prima."""
    if n < 2:
        return False
    # Memperbaiki logika loop dengan akar kuadrat dan range yang tepat
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def average(numbers):
    """Menghitung rata-rata dari list angka."""
    if not numbers:
        return 0
    # Menggunakan sum() dan membagi dengan jumlah elemen yang benar
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """Mencari nilai maksimum dalam list."""
    if not numbers:
        return None
    # Inisialisasi dengan elemen pertama agar bekerja untuk angka negatif
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


def factorial(n):
    """Menghitung faktorial dari n."""
    if n < 0:
        return None
    result = 1
    # Loop dimulai dari 1 agar tidak mengalikan dengan 0
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("is_prime(9) =", is_prime(9))          # False
    print("average([2,4,6]) =", average([2, 4, 6]))  # 4.0
    print("find_max([-5,-2,-9]) =", find_max([-5, -2, -9]))  # -2
    print("factorial(5) =", factorial(5))         # 120
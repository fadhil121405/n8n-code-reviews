"""
bug1_kalkulasi.py
Berisi fungsi-fungsi kalkulasi sederhana.
File ini SENGAJA mengandung bug untuk keperluan testing AI agent.
"""


def is_prime(n):
    """Cek apakah n adalah bilangan prima."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def average(numbers):
    """Menghitung rata-rata dari list angka."""
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_max(numbers):
    """Mencari nilai maksimum dalam list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


def factorial(n):
    """Menghitung faktorial dari n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("is_prime(9) =", is_prime(9))          # seharusnya False, tapi bug bikin True
    print("average([2,4,6]) =", average([2, 4, 6]))  # seharusnya 4.0
    print("find_max([-5,-2,-9]) =", find_max([-5, -2, -9]))  # seharusnya -2
    print("factorial(5) =", factorial(5))         # seharusnya 120
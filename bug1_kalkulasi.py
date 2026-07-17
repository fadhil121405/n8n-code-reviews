
def is_prime(n):
    """Cek apakah n adalah bilangan prima."""
    if n < 2:
        return False
    # Memperbaiki range hingga int(n**0.5) + 1 agar efisien dan akurat
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def average(numbers):
    """Menghitung rata-rata dari list angka."""
    if not numbers:
        return 0
    # Menggunakan sum() dan len() untuk akurasi
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """Mencari nilai maksimum dalam list."""
    if not numbers:
        return None
    # Inisialisasi dengan elemen pertama agar mendukung angka negatif
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


def factorial(n):
    """Menghitung faktorial dari n."""
    result = 1
    # Memperbaiki loop agar dimulai dari 1 hingga n
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("is_prime(9) =", is_prime(9))          # Output: False
    print("average([2,4,6]) =", average([2, 4, 6]))  # Output: 4.0
    print("find_max([-5,-2,-9]) =", find_max([-5, -2, -9]))  # Output: -2
    print("factorial(5) =", factorial(5))         # Output: 120
    
    
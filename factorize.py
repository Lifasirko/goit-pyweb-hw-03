import time
from multiprocessing import Pool, cpu_count


def factorize_number(number):
    """Функція для факторизації числа."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_sync(numbers):
    """Синхронна версія функції факторизації."""
    return [factorize_number(number) for number in numbers]


def factorize_async(numbers):
    """Асинхронна версія функції факторизації з використанням multiprocessing."""

    with Pool(processes=cpu_count()) as pool:
        result = pool.map(factorize_number, numbers)
    return result


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060, 1548956211]

    print(f"Кількість ядер - {cpu_count()}")

    start_time_sync = time.time()
    results_sync = factorize_sync(numbers)
    end_time_sync = time.time()
    duration_sync = end_time_sync - start_time_sync
    print(f"Synchronous execution time: {duration_sync} seconds")

    start_time_async = time.time()
    results_parallel = factorize_async(numbers)
    end_time_async = time.time()
    duration_async = end_time_async - start_time_async
    print(f"Parallel execution time: {duration_async} seconds")

    dur_diff = duration_sync - duration_async
    print(f"Синхронна функція виконувалась довше на {dur_diff} секунд")

    for result in results_sync:
        print(result)

# Вхідний список чисел
# numbers = [128, 255, 99999, 10651060]


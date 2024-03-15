import concurrent.futures
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


def factorize_async(n):
    """Асинхронна версія функції факторизації з використанням multiprocessing."""

    with concurrent.futures.ProcessPoolExecutor(cpu_count()) as executor:
        res = zip(n, executor.map(factorize_number, n))
    return res
    # with Pool(processes=cpu_count()) as pool:
    #     res = pool.map(factorize_number, n)
    # return res


def main():
    numbers = [128, 255, 99999, 10651060, 154895621]

    print(f"Кількість ядер - {cpu_count()}")

    start_time_sync = time.time()
    results_sync = factorize_sync(numbers)
    end_time_sync = time.time()
    duration_sync = end_time_sync - start_time_sync
    print(f"Synchronous execution time: {duration_sync} seconds")
    for result in results_sync:
        print(f"results_sync: {result}")

    start_time_async = time.time()
    results_parallel = factorize_async(numbers)
    end_time_async = time.time()
    duration_async = end_time_async - start_time_async
    print(f"Parallel execution time: {duration_async} seconds")
    for result in results_parallel:
        print(f"results_parallel: {result}")

    dur_diff = duration_sync - duration_async
    print(f"Синхронна функція виконувалась довше на {dur_diff} секунд")


# Вхідний список чисел
# numbers = [128, 255, 99999, 10651060]

if __name__ == "__main__":
    main()

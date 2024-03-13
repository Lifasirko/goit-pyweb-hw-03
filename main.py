import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import sys


def copy_file(file_path, target_dir):
    """
    Копіює файл у цільову директорію згідно його розширення.
    """
    # Визначення цільової піддиректорії за розширенням файлу
    extension = os.path.splitext(file_path)[1][1:]
    target_subdir = os.path.join(target_dir, extension)

    # Створення цільової піддиректорії, якщо вона не існує
    if not os.path.exists(target_subdir):
        os.makedirs(target_subdir)

    # Копіювання файлу
    shutil.copy(file_path, target_subdir)


def process_directory(source_dir, target_dir):
    """
    Обробляє всі файли в директорії рекурсивно, використовуючи ThreadPoolExecutor для багатопотоковості.
    """
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path, target_dir)


if __name__ == "__main__":
    # Читання аргументів командного рядка
    if len(sys.argv) > 2:
        source_dir = sys.argv[1]
        target_dir = sys.argv[2]
    else:
        print("Використання: python script.py <шлях до джерельної директорії> <шлях до цільової директорії>")
        sys.exit(1)

    # Запуск обробки
    process_directory(source_dir, target_dir)
    print("Обробку завершено.")


# python main.py
# C:\Users\MikeK\OneDrive\Робочий стіл\Навчання\Маркетинг для соцмереж\Відео
# D:\one\target

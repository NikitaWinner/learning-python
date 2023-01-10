import os

def count_size(dir: str) -> dict:
    """
    Функция сбора статистики размеров файлов по папке.
    Возвращает словарь с непустыми значениями
    """
    size_value = {10 ** x: 0 for x in range(1, 7)}
    all_files = [item for item in os.scandir(dir)]
    for filename in all_files:
        size = filename.stat().st_size
        for key in sorted(size_value.keys()):
            if size > key:
                continue
            else:
                size_value[key] += 1
                break

    return {threshold: count for threshold, count in sorted(size_value.items()) if count}

if __name__ == '__main__':
    base_dir = 'some_data'
    print(count_size(base_dir))



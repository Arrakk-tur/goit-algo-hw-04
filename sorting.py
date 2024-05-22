import timeit
import random


# Функції сортування
def merge_sort(arr):
    # Сортування злиттям

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    # Сортування вставками

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def measure_time(sort_func, data):
    # Вимірювання часу виконання

    start_time = timeit.default_timer()
    sort_func(data)
    return timeit.default_timer() - start_time


# Створення тестових даних
sizes = [100, 1000, 10000]
results = []

for size in sizes:
    data = random.sample(range(size * 10), size)
    data_1 = data[:]

    time_merge_sort = measure_time(merge_sort, data[:])
    time_insertion_sort = measure_time(insertion_sort, data_1[:])
    time_timsort = measure_time(sorted, data[:])

    results.append((size, time_merge_sort, time_insertion_sort, time_timsort))

# Виведення результатів
for size, time_merge, time_insert, time_tim in results:
    print(f"Size: {size}")
    print(f"Merge Sort Time: {time_merge:.6f} seconds")
    print(f"Insertion Sort Time: {time_insert:.6f} seconds")
    print(f"Timsort Time: {time_tim:.6f} seconds")
    print("---")

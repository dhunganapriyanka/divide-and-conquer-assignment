import random
import time
import tracemalloc


# -------------------------------------------------
# Merge Sort
# -------------------------------------------------

def merge_sort(arr):
    # Base case: a list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -------------------------------------------------
# Quick Sort
# -------------------------------------------------

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Use the middle element as the pivot
    # This helps avoid very bad recursion
    # on sorted and reverse-sorted data.
    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for value in arr:

        if value < pivot:
            left.append(value)

        elif value == pivot:
            middle.append(value)

        else:
            right.append(value)

    return (
        quick_sort(left)
        + middle
        + quick_sort(right)
    )


# -------------------------------------------------
# Performance Testing Function
# -------------------------------------------------

def test_algorithm(function, data):

    tracemalloc.start()

    start_time = time.perf_counter()

    sorted_result = function(data.copy())

    end_time = time.perf_counter()

    current_memory, peak_memory = (
        tracemalloc.get_traced_memory()
    )

    tracemalloc.stop()

    execution_time = end_time - start_time

    memory_usage = peak_memory / 1024

    return sorted_result, execution_time, memory_usage


# -------------------------------------------------
# Dataset Sizes
# -------------------------------------------------

sizes = [1000, 5000, 10000]


# -------------------------------------------------
# Run Tests
# -------------------------------------------------

for size in sizes:

    print("\n")
    print("=" * 60)
    print("DATASET SIZE:", size)
    print("=" * 60)

    # Create datasets
    sorted_data = list(range(size))

    reverse_data = list(
        range(size, 0, -1)
    )

    random_data = random.sample(
        range(size * 10),
        size
    )

    datasets = {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_data,
        "Random": random_data
    }

    # ---------------------------------------------
    # Merge Sort Tests
    # ---------------------------------------------

    print("\nMERGE SORT RESULTS")

    for dataset_name, data in datasets.items():

        result, execution_time, memory = (
            test_algorithm(
                merge_sort,
                data
            )
        )

        print(
            f"{dataset_name}: "
            f"Time = {execution_time:.6f} seconds, "
            f"Memory = {memory:.2f} KB"
        )

    # ---------------------------------------------
    # Quick Sort Tests
    # ---------------------------------------------

    print("\nQUICK SORT RESULTS")

    for dataset_name, data in datasets.items():

        result, execution_time, memory = (
            test_algorithm(
                quick_sort,
                data
            )
        )

        print(
            f"{dataset_name}: "
            f"Time = {execution_time:.6f} seconds, "
            f"Memory = {memory:.2f} KB"
        )


print("\n")
print("=" * 60)
print("PERFORMANCE TESTING COMPLETED")
print("=" * 60)

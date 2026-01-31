import numpy as np


#### BUBBLE SORT ####
def bubble_sort(arr):
    intermediate_arrays = []
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intermediate_arrays.append(arr.copy())
    return intermediate_arrays


#### BUBBLE REVERSE ####
def bubble_sort_reverse(arr):
    intermediate_arrays = []
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                intermediate_arrays.append(arr.copy())
    return intermediate_arrays


#### COCKTAIL SHAKER SORT ####
def cocktail_shaker(arr):
    intermediate_arrays = []
    swapped = True
    start = 0
    end = len(arr) - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intermediate_arrays.append(arr.copy())
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                intermediate_arrays.append(arr.copy())
                swapped = True
        start += 1
    return intermediate_arrays


#### SELECTION SORT ####
def selection_sort(arr):
    intermediate_arrays = []
    for i in range(len(arr)):
        min_idx = i + np.argmin(arr[i:])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intermediate_arrays.append(arr.copy())
    return intermediate_arrays


#### INSERTION SORT ####
def insertion_sort(arr):
    intermediate_arrays = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            intermediate_arrays.append(arr.copy())
        arr[j + 1] = key
        intermediate_arrays.append(arr.copy())
    return intermediate_arrays


#### QUICK SORT ####
def partition(arr, low, high, intermediate_arrays):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            intermediate_arrays.append(arr.copy())
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    intermediate_arrays.append(arr.copy())
    return i + 1

def quick_sort_recursive(arr, low, high, intermediate_arrays):
    if low < high:
        pivot_index = partition(arr, low, high, intermediate_arrays)
        quick_sort_recursive(arr, low, pivot_index - 1, intermediate_arrays)
        quick_sort_recursive(arr, pivot_index + 1, high, intermediate_arrays)

def quick_sort(arr):
    intermediate_arrays = []
    quick_sort_recursive(arr, 0, len(arr) - 1, intermediate_arrays)
    return intermediate_arrays


#### HEAP SORT ####
def heapify(arr, n, i, intermediate_arrays):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        intermediate_arrays.append(arr.copy())
        heapify(arr, n, largest, intermediate_arrays)

def heap_sort(arr):
    intermediate_arrays = []
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i, intermediate_arrays)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        intermediate_arrays.append(arr.copy())
        heapify(arr, i, 0, intermediate_arrays)
    return intermediate_arrays


#### MERGE SORT ####
def merge(arr, start, mid, end, intermediate_arrays):
    temp_start = mid + 1
    if arr[mid] <= arr[temp_start]:
        return
    while start <= mid and temp_start <= end:
        if arr[start] <= arr[temp_start]:
            start += 1
        else:
            value = arr[temp_start]
            index = temp_start
            while index != start:
                arr[index] = arr[index - 1]
                intermediate_arrays.append(arr.copy())
                index -= 1
            arr[start] = value
            intermediate_arrays.append(arr.copy())
            start += 1
            mid += 1
            temp_start += 1


def merge_sort(arr, start_idx=0, end_idx=None, intermediate_arrays=None):
    intermediate_arrays = [] if intermediate_arrays is None else intermediate_arrays
    end_idx = len(arr) - 1 if end_idx is None else end_idx
    if start_idx < end_idx:
        center = start_idx + (end_idx - start_idx) // 2
        merge_sort(arr, start_idx, center, intermediate_arrays)
        merge_sort(arr, center + 1, end_idx, intermediate_arrays)
        merge(arr, start_idx, center, end_idx, intermediate_arrays)
    return intermediate_arrays


#### RADIX SORT ####
def perform_counting_sort(arr, exp, intermediate_arrays):
    n = len(arr)
    output = [0] * n
    count = [0] * n
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    intermediate_arrays.append(count.copy())
    for i in range(1, 10):
        count[i] += count[i - 1]
        intermediate_arrays.append(count.copy())
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    intermediate_arrays.append(output.copy())
    arr[:] = output[:]

def radix_sort(arr):
    intermediate_arrays = []
    max_elem = max(arr)
    exp = 1
    while max_elem / exp >= 1:
        perform_counting_sort(arr, exp, intermediate_arrays)
        exp *= 10
    return intermediate_arrays


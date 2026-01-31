import random
from sorting_algorithms import *


def create_rand_array(size):
    return [random.randrange(0, size) for _ in range(size)]

def generate_unsorted_arrays(size, num_array):
    return [create_rand_array(size) for _ in range(num_array)]

def sort_equal_arrays(array_size):
    array = create_rand_array(array_size)
    return {
        'bubble_sort': bubble_sort(array.copy()),
        'bubble_sort_reverse': bubble_sort_reverse(array.copy()),
        'cocktail_shaker': cocktail_shaker(array.copy()),
        'selection_sort': selection_sort(array.copy()),
        'quick_sort': quick_sort(array.copy()),
        'heap_sort': heap_sort(array.copy()),
        'insertion_sort': insertion_sort(array.copy()),
        'merge_sort': merge_sort(array.copy()),
        'radix_sort': radix_sort(array.copy())
    }

def sort_distinct_arrays(size, num_arrays):
    arrays = generate_unsorted_arrays(size, num_arrays)
    return {
        'bubble_sort': bubble_sort(arrays[0].copy()),
        'bubble_sort_reverse': bubble_sort_reverse(arrays[1].copy()),
        'cocktail_shaker': cocktail_shaker(arrays[4].copy()),
        'selection_sort': selection_sort(arrays[2].copy()),
        'quick_sort': quick_sort(arrays[5].copy()),
        'heap_sort': heap_sort(arrays[6].copy()),
        'insertion_sort': insertion_sort(arrays[3].copy()),
        'merge_sort': merge_sort(arrays[7].copy()),
        'radix_sort': radix_sort(arrays[8].copy())
    }

def sort_arrays(size, num_arrays, distinct=False):
    if distinct:
        return sort_distinct_arrays(size, num_arrays)
    return sort_equal_arrays(size)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализация алгоритма Heap Sort: Спроектируйте и реализуйте алгоритм
# сортировки кучей (Heap Sort) на любом удобном для вас языке программирования.
# После этого протестируйте вашу реализацию на различных видах входных данных,
# таких как отсортированный массив, массив в обратном порядке и случайный.
# Оцените эффективность алгоритма в каждом случае.

import timeit
import numpy as np
import matplotlib.pyplot as plt
import random


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def measure_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=100) / 100


def find_coeffs(xs, ys):
    sx = sum(xs)
    stime = sum(ys)
    sx2 = sum(i**2 for i in xs)
    sxtime = sum(i*j for i, j in zip(xs, ys))
    n = len(xs)
    matrixx = [[sx2, sx], [sx, n]]
    matrixy = [[sxtime], [stime]]
    x = np.linalg.solve(matrixx, matrixy)
    return x[0][0], x[1][0]


def analyze_sort(start, end, step):
    sizes = list(range(start, end + 1, step))
    times_avg = []
    times_worst = []
    times_rnd = []

    for size in sizes:

        arr = list(range(size))
        time_avg = measure_time(heap_sort, arr)

        arr_reverse = arr[::-1]
        time_worst = measure_time(heap_sort, arr_reverse)

        random.shuffle(arr)
        time_rnd = measure_time(heap_sort, arr)

        times_avg.append(time_avg)
        times_worst.append(time_worst)
        times_rnd.append(time_rnd)

    return sizes, times_avg, times_worst, times_rnd


def plot_results(sizes, times_avg, times_worst, times_rnd):
    plt.figure()
    plt.scatter(sizes, times_avg, label='Отсортированный массив', s=10)
    a_avg, b_avg = find_coeffs(sizes, times_avg)
    y_avg = a_avg * np.array(sizes) + b_avg
    plt.plot(sizes, y_avg, label=f'{a_avg:.9f} * x + {b_avg:.9f}', color='red')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Отсортированный массив')
    plt.legend()

    # Plot for reverse sorted array
    plt.figure()
    plt.scatter(sizes, times_worst, label='Несортированный массив', s=10)
    a_worst, b_worst = find_coeffs(sizes, times_worst)
    y_worst = a_worst * np.array(sizes) + b_worst
    plt.plot(sizes, y_worst, label=f'{a_worst:.9f} * x + {b_worst:.9f}',
             color='blue')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Несортированный массив')
    plt.legend()

    # Plot for random array
    plt.figure()
    plt.scatter(sizes, times_rnd, label='Случайный массив', s=10)
    a_rnd, b_rnd = find_coeffs(sizes, times_rnd)
    y_rnd = a_rnd * np.array(sizes) + b_rnd
    plt.plot(sizes, y_rnd, label=f'{a_rnd:.9f} * x + {b_rnd:.9f}',
             color='green')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Случайный массив')
    plt.legend()

    plt.show()


if __name__ == '__main__':

    start = 100
    end = 1000
    step = 10

    sizes, times_avg, times_worst, times_rnd = analyze_sort(start, end, step)
    plot_results(sizes, times_avg, times_worst, times_rnd)

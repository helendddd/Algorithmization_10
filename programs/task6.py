#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны массивы A[1...n] и B[1...n]. Мы хотим вывести все n2 сумм вида A[i]+B[j]
# в возрастающем порядке. Наивный способ — создать массив, содержащий все
# такие суммы, и отсортировать его. Соответствующий алгоритм имеет время
# работы O(n2logn) и использует O(n2) памяти. Приведите алгоритм с таким же
# временем работы, который использует линейную память.

import random


def merge_and_sort(A, B):
    result = []
    n = len(A)

    for i in range(n):
        for j in range(n):
            result.append(A[i] + B[j])

    result = merge_sort(result)

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

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


if __name__ == '__main__':
    n = int(input("Enter n... "))
    A = list(range(n))
    B = list(range(n))
    random.shuffle(A)
    random.shuffle(B)
    result = merge_and_sort(A, B)
    print(result)

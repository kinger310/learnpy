# -*- coding: utf-8 -*-

from learnmodule.fibo import fib

def bubble_sort(numbers):
    for j in range(len(numbers)-1, -1, -1):
        for i in range(j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


# %%


def search(seq, number, low=0, high=None):
    if high is None:
        high = len(seq) - 1
    if low == high:
        assert number == seq[high]
        return high
    else:
        middle = (low + high) // 2
        if number <= seq[middle]:
            return search(seq, number, low, middle)
        else:
            return search(seq, number, middle+1, high)
# %%


def main():
    numbers = [4, 2, 8, 9, 10, 3, 1, 5, 7, 6]
    bubble_sort(numbers)
    print(numbers)

if __name__ == '__main__':
    main()
    a = list(range(1, 101, 3))
    search(a, 25)

# -*- coding: utf-8 -*-


def bubbleSort(numbers):
    for j in range(len(numbers)-1, -1, -1):
        for i in range(j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


def main():
    from fibo import fib
    fib(100)
    numbers = [4, 2, 8, 9, 10, 3, 1, 5, 7, 6]
    bubbleSort(numbers)
    print(numbers)

if __name__ == '__main__':
    main()

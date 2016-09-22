import random


def minimum(arr):
    minim = arr[0]
    for el in arr:
        if el < minim:
            minim = el
    return minim


def average(arr, m):
    s = 0
    for el in arr:
        s += el
    return s/m


n = int(input("Размер массива "))
arr1 = list(range(n))
for i in arr1:
    arr1[i] = random.randint(0, 10)
print(arr1)
print("Наименьший элемент ", minimum(arr1))
print("Среднее арифметическое ", average(arr1,n))
n = int(input("Размер массива "))
arr1 = list(range(n))
for i in arr1:
    arr1[i] = random.randint(0, 10)
print(arr1)
print("Наименьший элемент ", minimum(arr1))
print("Среднее арифметическое ", average(arr1,n))
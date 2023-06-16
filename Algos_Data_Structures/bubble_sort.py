import time
from Timsort import timsort
import random


def bubble_sort(numbers):
    swap = True
    while swap:
        for i in range(len(numbers)-1):
            for number in range(len(numbers)-i-1):
                if numbers[number] > numbers[number+1]:
                    temp = numbers[number]
                    numbers[number] = numbers[number+1]
                    numbers[number+1] = temp
                    swap = True
                else:
                    swap = False

    return numbers


def randomlist():
    return [random.randint(0, 100000) for _ in range(1000)]


arr = randomlist()
start = time.time()
print(sorted(arr))
end = time.time()
pysort_time = end-start
print(f'sorted in {pysort_time}')

start = time.time()
print(bubble_sort(arr))
end = time.time()
bubble_sort_time = end-start
print(f'Bubble sorted in {bubble_sort_time}')

start = time.time()
print(timsort(arr))
end = time.time()
timsort_time = end - start
print(f'Timsorted in {timsort_time}')

fastest_time = sorted([pysort_time, bubble_sort_time, timsort_time])

if fastest_time[0] == bubble_sort_time:
    print(f'Bubble sort is the fastest')
elif fastest_time[0] == timsort_time:
    print(f'timsort is the fastest')
else:
    print(f'Sorted is the fastest')

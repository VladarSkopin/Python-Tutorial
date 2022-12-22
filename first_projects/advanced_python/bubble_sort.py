def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


arr = [10, 3, 4, 80, 5, 1, 12, 30]
bubble_sort(arr)
print(arr)  # [1, 3, 4, 5, 10, 12, 30, 80]

def merge_sort(array): 
    if len(array) >1: 
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]: 
                array[k] = L[i] 
                i+=1
            else: 
                array[k] = R[j] 
                j+=1
            k+=1

        while i < len(L): 
            array[k] = L[i] 
            i+=1
            k+=1

        while j < len(R): 
            array[k] = R[j] 
            j+=1
            k+=1



def make_heap(array, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]: 
        largest = l 

    if r < n and array[largest] < array[r]: 
        largest = r 

    if largest != i: 
        array[i],array[largest] = array[largest],array[i]

        make_heap(array, n, largest) 


def heap_sort(array): 
    n = len(array) 

    for i in range(n, -1, -1): 
        make_heap(array, n, i) 

    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i]
        make_heap(array, i, 0)



def partition(array, low, high): 
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:  
            i = i + 1 
            array[i], array[j] = array[j], array[i] 

    array[i+1], array[high] = array[high], array[i+1] 
    return (i + 1) 

def quick_sort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high) 
        quick_sort(arr, low, pi - 1) 
        quick_sort(arr, pi + 1, high)




import time
from datetime import datetime

f = open(r"C:\Users\chmat\OneDrive\Рабочий стол\Теория алгоритмов\Programs\LogarithmicSortingAlgorithms\ai182.txt", "r")
f.seek(372)
s = f.read(15)
original_array = [int (s[i]) for i in range (0, 15)]

#Merge sort
#Average duration: 0:00:00.000995
array = original_array
start_time = datetime.now()
merge_sort(array)
end_time = datetime.now()
print("Merge sort: " + str(array) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Heap sort
#Average duration: 0:00:00.000500
array = original_array
start_time = datetime.now()
heap_sort(array)
end_time = datetime.now()
print("Heap sort: " + str(array) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Quick sort
#Average duration: 0:00:00.000995
array = original_array
start_time = datetime.now()
quick_sort(array, 0, len(array) - 1)
end_time = datetime.now()
print("Quick sort: " + str(array) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

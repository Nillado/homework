import time
from datetime import datetime


def mergeSort(massive):

    if len(massive)>1:
        mid = len(massive)//2
        lefthalf = massive[:mid]
        righthalf = massive[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                massive[k]=lefthalf[i]
                i=i+1
            else:
                massive[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            massive[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            massive[k]=righthalf[j]
            j=j+1
            k=k+1


def make_heap(massive, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and massive[largest] < massive[l]: 
        largest = l 

    if r < n and massive[largest] < massive[r]: 
        largest = r 

    if largest != i: 
        massive[i],massive[largest] = massive[largest],massive[i]

        make_heap(massive, n, largest) 


def heap_sort(massive): 
    n = len(massive) 

    for i in range(n, -1, -1): 
        make_heap(massive, n, i) 

    for i in range(n-1, 0, -1): 
        massive[i], massive[0] = massive[0], massive[i]
        make_heap(massive, i, 0)



def partition(massive, low, high): 
    i = (low - 1)
    pivot = massive[high]

    for j in range(low, high):
        if massive[j] <= pivot:  
            i = i + 1 
            massive[i], massive[j] = massive[j], massive[i] 

    massive[i+1], massive[high] = massive[high], massive[i+1] 
    return (i + 1) 

def quick_sort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high) 
        quick_sort(arr, low, pi - 1) 
        quick_sort(arr, pi + 1, high)


file = open("ai183.txt", "r")
someMassive = []

while True:
    if file.read(1) == '2':
        if file.read(2) == ': ':
            symbol = file.read(1)

            while symbol != '}':
                someMassive.append(int(symbol))
                symbol = file.read(1)

            break

file.close()


#Merge sort
#Average duration: 0:00:00.0001005
massive = someMassive
start_time = datetime.now()
mergeSort(massive)
end_time = datetime.now()
print("Merge sort: " + str(massive) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Heap sort
#Average duration: 0:00:00.0001019
massive = someMassive
start_time = datetime.now()
heap_sort(massive)
end_time = datetime.now()
print("Heap sort: " + str(massive) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")

#Quick sort
#Average duration: 0:00:00.001000
massive = someMassive
start_time = datetime.now()
quick_sort(massive, 0, len(massive) - 1)
end_time = datetime.now()
print("Quick sort: " + str(massive) + "\n" + 'Duration: {}'.format(end_time - start_time) + "\n")





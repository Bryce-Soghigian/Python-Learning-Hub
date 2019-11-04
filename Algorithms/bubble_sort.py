"""
Explaination of algorithm
Loops through an array of data
compares each value side by side
and flips the greater and lower value
until all the values are sorted


Space complexity == O(1)

Time complexity == Θ(n^2)

"""
#While Loop solution
def while_bubble_sort( arr ):
    lastUnsorted = len(arr) -1
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(lastUnsorted):
            if arr[i]> arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
                isSorted = False
            
    lastUnsorted -= 1
#nested Loop solution
def bubble_sort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)
"""
Javascript Solution


"""
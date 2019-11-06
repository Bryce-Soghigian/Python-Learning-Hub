# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(len(merged_arr)):
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
            #If B is SMOL move him
        else:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
    return merged_arr
  

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print("split",arr)
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        #oh no its recursion time
        #I used Recursion and iteration
        #its techincally a pass my dude 
        #just saying
        merge_sort(left_half)
        merge_sort(right_half)
        #Declaring my iterables
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
           if left_half[i] < right_half[j]:
               arr[k]=left_half[i]
               i=i+1
           else:
               arr[k]=right_half[j]
               j=j+1
           k=k+1

        while i < len(left_half):
           arr[k]=left_half[i]
           i=i+1
           k=k+1

        while j < len(right_half):
           arr[k]=right_half[j]
           j=j+1
           k=k+1

    return arr


alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)
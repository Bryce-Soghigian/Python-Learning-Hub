"""
Javascript Solution:
a = [16, 19, 11, 15, 10, 12, 14]
const insertion_sort = (ar) => {
    for(let i=0;i<ar.length;i++){
        j=a.index(i)
        while(j>0):
            if (a[j-1]> a[j]){
                a[j-1],a[j] = a[j],a[j-1]
            }else{
                break
            j = j-1
            }
            return ar
    }
}
insertion_sort(a)


Complexity:

    Space Complexity == 0(1)
    Time Complexity == Θ(n^2)




"""




a = [16, 19, 11, 15, 10, 12, 14]

#iterating over a
for i in a:
    j = a.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
print (a)

#Recursive insertion sort
ar = [1,2,6,7,89,32,13]
def recursive_insertion_sort(arr,n):
    #base case
    if n<=1:
        return
    #sorting the first n-1 ele
    recursive_insertion_sort(arr,n-1)
    #insert last ele in correct postion in sorted arr
    last = arr[n-1]
    j= n-2
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position
    while(j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = last



def printArray(arr,n): 
    for i in range(n): 
        print(arr[i],)  
  
# Driver program to test insertion sort  
#Testing my sorted
arr = [12,11,13,5,6] 
n = len(arr) 
recursive_insertion_sort(arr, n) 
printArray(arr, n) 


"""explaining the code
for i in a: // Here we are iterating through a list

while j>0
//Index of the current element is positive. This means
that the element at the index of 'j' is not the first
element and we need to compare the values

if a[j-1] > a[j] // These Two elements are not in order.
We need to swap them. 

else // The elements are in order and we can break the loop

a[j-1],a[j] = a[j],a[j-1]//Swapping function
"""
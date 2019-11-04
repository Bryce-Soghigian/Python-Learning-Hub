"""Notes:
This algorithm will repeatedly find the minimun
ele from the unsorted part and 
throw it at the start. This algorithm works with 
two separate sub arrays in a given array

The lists:
    1. The sorted subarray
    2. Remaining subarray which hasn't been sorted yet


Complexity: 
    Time Complexity = Θ(n^2)
    Space Complexity = 0(1)


"""

"""JS Selection sort
const sort = (arr) => {
    for(let i = 0;i<arr.length;i++){
       let min = i
       for(let j = 0;i+1<arr.length;j+1){
           if(arr[min]> arr[j]){
               min = j
           }
           #swap values
       arr[i], arr[min] = arr[min], arr[i]
       } 
    }
}


"""
#Iterative Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]



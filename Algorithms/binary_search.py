"""
const binary_search = (arr,kw) => {
let low = 0
high = arr.length -1
while(low<=high){
    let middle = (low+high)/2
    if(kw<arr[middle]){
        high = middle - 1
    }else if{
        low = middle +1
    }else{
        return middle
    }
}

}


"""

def binary_search(arr,keyword):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low+high)/2
        if keyword < arr[middle]:
            high = middle - 1
        elif keyword > arr[middle]:
            low = middle + 1
        else:
            return middle
    return "Not found"


"""
Even though we have a loop inside our function we get a 
runtime of O(log(n))
Its because we only have to iterate through half the values
"""



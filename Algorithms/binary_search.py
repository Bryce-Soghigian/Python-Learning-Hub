"""
const binary_search = (arr,kw) => {
let low = 0
high = arr.length -1
while(low<=high){
    let middle = (low+high)/2
    if(kw<arr[middle]){
        high = middle - 1
    }else if(kw>arr[middle]){
        low = middle +1
    }else{
        return middle
    }
}

}

Complexity:
    Space Complexity == O(1)
    Time Complexity == O(Log n)

"""
"""
Explain The interative approach:
we set up a low and a high
low = first index aka arr[0]
high is the length of the arr -1 (arr starts at 0 rather than 1)
we then set up a while loop that while low is still lower or not equal to high 
we interate through it. 
we then declare our middle variable middle = (low+high)/2  //This is just the center of our list
if keyword < arr[middle]:
    we use this to find a new high of our list based on the current middle
 elif keyword > arr[middle]: 
     remember our while loops condition. We also need to find the new low
if it gets through those blocks we have found our Keyword
unless it doesn't exist


"""
#Interative Approach
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


def recursive_binary_search(arr, l, r, kw):
    if r>= 1:
        
        middle = 1+ (r-1)/2

        #If Element is present at the middle
        if arr[middle] == kw:
            return middle
        
        elif arr[middle] > kw:
            return recursive_binary_search(arr,l, middle-1, kw)

        else:
            return recursive_binary_search(arr, middle+1, r, kw)

    else:
        print("not found")
        return f"Sorry {kw} isn't within this list"


"""
Explain The algorithm:
    Recursive
First We compare our keyword with the middle ele
-if our kw == middle we return the middle index of list
-elif x is greater than the mid ele then x can only lie in 
the right half of the subarray
-Else x is smaller and we recur for the left half


"""
#Runtime
"""
Even though we have a loop inside our function we get a 
runtime of O(log(n))
Its because we only have to iterate through half the values
"""



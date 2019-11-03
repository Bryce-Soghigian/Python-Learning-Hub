#kw is some keyword 
#array is some data structure
"""
Javascript Solution

const linear_search = (arr, kw) => {
    for(let i = 0; i<arr.length; i++){
        if(arr[i]===kw){
            return kw
        }else{
            return "keyword doesn't exist within arr"
        }
    }
} 



"""
array = [1,2,4,5,6]
#Python Solution

def linear_search(arr,kw):
    for i in range(0, len(arr)-1):
        if i == kw:
            print(kw)
            return kw
        else:
            return f"Keyword doesn't exist in the array"


linear_search(array,2)
#Output === 2
#this is O(n) is most cases
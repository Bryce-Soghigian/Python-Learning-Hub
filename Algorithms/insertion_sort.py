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
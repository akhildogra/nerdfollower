#This code could be used to search for an item in a given sorted list
#this method of searching is known as binary search
def bsearch(seq,v,l,r):
    #Here seq is the name of the given list
    #v is the value that we need to find in the given sequence
    #l and r is index of the sliced sequence if we want to, otherwise keep l = 0 and r = len(seq) -1 or a number greater than that
    if (r-l ==0):
        return(False)# if the sliced sequence does not has any element then obviously we can't find the value
    mid = r+l//2 # to have integer division so that no float number appears. It gives us the quotient
    if (v== seq[mid]):
        return(True)# if the middle value is the value that we need to find
    elif(v< seq[mid]):
        return(bsearch(seq,v,l,mid))# recursion up to a point till there is only one value left in the sliced sequence
    else:
        return(bsearch(seq,v,mid+1,r))# if the value is in the second part of the sequence.
#time taken to reach to the value depends on the size of the list and what the value is.
#T(0) = 0
#T(n) = 1+ T(n/2)
#these two steps together are commonly known as recurrance
#it takes log2(n) steps to reach to the value considering the worst case in a sorted list and also considering that built in list
#is a type of array

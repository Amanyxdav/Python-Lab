def Binary_search(a,start, end, x):
    mid = (start + end )//2
    
    if a[mid] == x:
        print("element found at index", mid)
        return
        
    elif a[mid]>x:
        Binary_search(a,start, mid-1, x)
            
    elif a[mid]<x:
        Binary_search(a,mid+1, end, x)
            

a = [11,11,11 ,13,63, 56, 78, 90, 84, 28, 34, 68, 69,  227, 97, 68, 74, 86]
a.sort()
print("The given list is = ", a)
x = int(input("Enter value to be searched"))
Binary_search(a,0,len(a)-1, x)

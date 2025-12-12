def reversevow(s):
    vowels='aeiouAEIOU'
    arr=list(s)
    l=0
    r=len(s)-1
    while l<r:
        while l<r and arr[l] not in vowels:
            l+=1
        while l<r and arr[r] not in vowels:
            r-=1
        if l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
    return ''.join(arr)
s=input("Enter the string ")
print(reversevow(s))

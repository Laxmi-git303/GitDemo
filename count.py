def countvowelsconsonants(s):
    vowels='aeiouAEIOU'
    v=c=0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v+=1
            else:
                c+=1
    return v,c
s=input("Enter the string")
print(countvowelsconsonants(s))
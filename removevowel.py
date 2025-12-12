def removevowel(s):
    vowel='aeiouAEIOU'
    ans=[]
    for ch in s:
        if ch not in vowel:
            ans.append(ch)
    return ''.join(ans)
s=input("Enter the string")
print(removevowel(s))


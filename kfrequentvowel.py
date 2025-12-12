from collections import Counter
def kfreq(s,k):
    vowel='aeiouAEIOU'
    arr=[]

    for ch in s:
        if ch in vowel:
            arr.append(ch.lower())
    count=Counter(arr)
    return count.most_common(k)
print(kfreq("This is an example sentence with vowels", 1  ))
from collections import Counter
s="banana"
# freq={}
# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
# print(max(freq, key=freq.get))   # key with highest value
c=Counter(s)
a=c.most_common(1)
print(a[0][1])

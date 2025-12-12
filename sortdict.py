d={"a":2,"b":1,"c":8}
sortedbyvalue=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print(sortedbyvalue)
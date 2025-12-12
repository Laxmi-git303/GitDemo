def check(ch):
    if not ch or len(ch)!=1:
        return False
    ch=ch.lower()
    if ch in ['a','e','i','o','u']:
        return True
    return False
ch=input("Enter the character")
print(check(ch))
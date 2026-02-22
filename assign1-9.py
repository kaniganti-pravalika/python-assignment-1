s=input()
t=input()
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    s = sorted(s)
    t = sorted(t)
    
    if s == t:
        return True
    else:
        return False

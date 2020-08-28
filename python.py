def findPairs(l,k):
    res=[]
    while l:
        num=l.pop()
        diff=k-num
        if diff in l:
            res.append((diff,num))
    return res
l=[1,5,3,7,9]
k=12
print(findPairs(l, 12))

def findpairs(L,k):
    res=[]
    while l:
        num=l.pop()
        diff=k-num
        if diff in l:
            res.append([diff,num])
    return res
l=[1,5,3,7,9]
k=12
print(findpairs(l,12))











            

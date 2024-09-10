xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True
print(res)
a = 15
b = -4
#print(a == (not b))
#print(a//b)
def solution(n):
    p = 0
    while(2**p < n):
        p+=1
    print(p)
    return n
solution(80)
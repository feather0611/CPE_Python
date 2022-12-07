def f(x:int):
    j = x%10
    k = x//10
    if (k>0):
        return j+f(k)
    return j

def g(x:int):
    j = f(x)
    k = j//10
    if (k==0):
        return j
    return g(j)

coll = []

while(True):
    a = input()
    if(a=='0'):
        break
    coll.append(a)

for ele in coll:
    print(g(int(ele)))
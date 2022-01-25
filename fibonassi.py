from functools import lru_cache


fibo_cache = {}
def fibonassi(n):
    #if we have cache the value then return it
    if n in fibo_cache:
        return fibo_cache[n]

    #Compute the Nth term

    if n == 1:
         value =1
    elif n ==2:
        value = 1
    elif n > 2:
        value = fibonassi(n -1) + fibonassi(n-2)
    
    #cache the value and return it
    fibo_cache[n] = value
    return value
@lru_cache
def fibonassi2(k):
    if k == 1:
        return 1
    elif k == 2:
        return 1
    elif k > 2:
        return fibonassi(k - 1) + fibonassi(k - 2)


for k in range(1, 51):
    ratio = fibonassi2(k+1)/ fibonassi2(k)
    print(ratio)
#    print(k, ":", fibonassi2(k))

for n in range(1, 6):
    print(n, ':', fibonassi(n))
    

    
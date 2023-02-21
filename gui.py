def f(L):
    cpt = 0
    for i in range(len(L)):
        cpt += 1
        L[cpt] += 2
        return L
print(f([1,2,3,4]))
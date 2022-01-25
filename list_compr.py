data = [(10, 'd'), (15, 'b'), (23, 'c'), (34, 'f')]

di = {'a':19, 'b': 21, 'e':6, 'r': 17}

print(sorted([(v,k) for k, v in di.items()],reverse=True))
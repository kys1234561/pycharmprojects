def odd_element(f):
    f1 = []
    for i in range(len(f)):
        if i % 2 == 0:
            f1.append(f[i])
    print(f1)
odd_element([1,2,3,4,6,7])
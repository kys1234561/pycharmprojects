def mul(a,b):
    try:
        c = a / b
        print(c)
    except:
        print('除数不能为零')

mul(3,2)
mul(2,0)
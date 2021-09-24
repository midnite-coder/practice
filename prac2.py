def myfunc(*args):
    str=[]
    for i in list(args):
        if i%2==0:
            str.append(i)
    return str
myfunc(1,2,3,4,5,6)
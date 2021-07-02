a=input("please enter a string:")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
y=most_frequent(a)
z=sorted(y,key=y.get,reverse=True)
for r in z:
    print(r,"=",y[r])

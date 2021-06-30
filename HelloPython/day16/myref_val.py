def callRef(a):
    a[0] =5
def callVal(a):
    a = 5

if __name__ == '__main__':
    a = [1]
    b = 1
    
    print(a)
    print(b)
    callRef(a)
    callVal(b)
    print(a)
    print(b)
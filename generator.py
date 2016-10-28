def get_fino():
    a,b = 0,1

    while True:
        yield a
        a,b = b,a+b

a = get_fino()

for i in a:
    print i

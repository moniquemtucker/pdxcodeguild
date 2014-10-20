a = 0
b = 20
while a <= b:
    print(b)
    b -= 1
    if b % 5 == 0 and b != 10:
        print(b)
        b -= 2
    elif b == 10:
        print('halfway done')
        b -= 2
    else:
        print(b)
        b -= 1
else:
    print('all done')



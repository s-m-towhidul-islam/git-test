def swap(a, b):
    print('before swapping: ', a, b)
    tmp = a
    a = b
    b = tmp
    print('after swapping: ', a, b)

a = 5
b = 10
swap(a,b)
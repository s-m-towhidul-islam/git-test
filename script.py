def swap(a, b):
    print('before swapping: ', a, b)
    a,b = b,a
    print('after swapping: ', a, b)

a = 5
b = 10
swap(a,b)
def swap(a, b):
    '''A function to swap values'''
    print('before swapping: ', a, b)
    #swapping the values
    a,b = b,a
    print('after swapping: ', a, b)

a = 5
b = 10
swap(a,b)
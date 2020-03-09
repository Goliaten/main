while True:
    x = int(input(''))
    b = (200+100*(x-2))*(x-1)
    c = 100*x**2-100*x
    x -= 1
    d = 100*x**2-100*x
    e = c-d
    print(b, c, e, ':')
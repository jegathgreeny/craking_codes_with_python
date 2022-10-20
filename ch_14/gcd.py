def gcd(a, b):
    while a != 0:
        a, b = b % a, a
        print(a, b)
    print(b)
    return b


# check
# gcd(24, 30)
# gcd(409119243, 87780243)
gcd(120, 50)

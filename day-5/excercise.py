def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
   return x * y // gcd(x, y) 

def is_prime(n):
    for factor in range(2,n):
        if n % factor:
            return False
    return True if n != 1 else False

if __name__ == '__main__':
    print("gcd(12, 8) = %d" % gcd(12, 8))
    print("lcm(12,8) = %d" % lcm(12, 8))
    print("is_prime(111) = %s" % is_prime(111))

def gen_primes():
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def largest_prime(x):
    p = gen_primes()
    p.__next__()
    a, b = 0, 1
    while b <= x:
        if x % b == 0:
            x = x / b
            a = b
            b = p.__next__()
        else:
            b = p.__next__()

    return a


# print(largest_prime(13195))
print(largest_prime(600851475143))

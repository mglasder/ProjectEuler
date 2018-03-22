"""
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def even_fibo(x):
    f = [1, 2]
    i = 2
    check = 3
    while check <= x:
        f.append(check)
        check = f[i] + f[i-1]
        i += 1

    for i in range(len(f)):
        if f[i] % 2 != 0:
            f[i] = 0

    print(f)
    return sum(f)


print(even_fibo(4000000))

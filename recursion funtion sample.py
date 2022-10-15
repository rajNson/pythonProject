def recursion(n):
    if n <= 1:
        return n
    else:
        return n + recursion(n - 1)

a = recursion(4)
print(a)



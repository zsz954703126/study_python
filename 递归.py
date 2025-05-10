def fun(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return fun(n-1)+fun(n-2)

print(fun(1))
print(fun(2))
print(fun(3))
print(fun(4))
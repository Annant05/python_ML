total = 0


def sum_re(var, b=10):
    global total
    total = var + b
    print(total + 5)


sum_re(5)
print(total)

def kangaroo(x1, v1, x2, v2):
    for i in range(1000):
        if x1 == x2:
            return "yess"
        x1 += v1
        x2 += v2
    return "no"
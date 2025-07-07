def countApplesAndOranges(s, t, a, b, apples, oranges):
    manzanas = 0
    naranjas = 0

    for i in apples:
        if s <= a + i <= t:
            manzanas += 1

    for i in oranges:
        if s <= b + i <= t:
            naranjas += 1

    print(manzanas)
    print(naranjas)
import string


def donuts(count):
    if count >= 10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: " + str(count)


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[len(s)-2:]

print("update number 2 for scenario test")
x = 'Chloe'
both_ends(x)


if __name__ == '__main__':
    main()
def test():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    toto = [[row[i] for row in matrix] for i in range(4)]
    print(toto)
    return toto
test()
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


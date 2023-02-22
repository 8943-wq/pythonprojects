l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
res = []


def sep(lst):
    for i in lst:
        if isinstance(i, list):
            sep(i)
        else:
            res.append(i)


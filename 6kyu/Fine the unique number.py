def find_uniq(xs):
    subset = set(xs)
    for s in subset:
        count = 0
        for x in xs:
            if s == x:
                count += 1
        if count == 1:
            return s

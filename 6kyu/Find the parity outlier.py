import random
def find_outlier(integers):
    count = 0
    for n in integers:
        if n % 2 == 0:
            count += 1
    if count >= 2:
        for n in integers:
            if n % 2 != 0:
                outlier = n
    else:
        for n in integers:
            if n % 2 == 0:
                outlier = n
    return outlier

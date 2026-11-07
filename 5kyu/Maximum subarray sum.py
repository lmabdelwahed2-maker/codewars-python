def max_sequence(arr):
    sum = 0
    if all(a < 0 for a in arr):
        return sum
    elif all(a >= 0 for a in arr):
        return sum(arr)
    else:
        sum_list = []
        for a in arr:
            sum += a
            if sum >= 0:
                sum_list.append(sum)
            elif sum < 0:
                sum = 0
                continue
        sum_list.sort()      
        return sum_list[-1]

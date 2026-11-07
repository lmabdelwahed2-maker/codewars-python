def solution(number):
    summ = 0
    for n in range (number):
        if n%3 == 0 or n%5 == 0:
            if n < 0:
                return 0
            else:
                summ += n
    return summ

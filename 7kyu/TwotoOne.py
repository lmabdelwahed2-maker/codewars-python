def longest(a1, a2):
    s1 = list(a1)
    s2 = list(a2)
    combined = s1 + s2
    final_list = sorted(set(combined))
    final_string = "".join(final_list)
    return final_string

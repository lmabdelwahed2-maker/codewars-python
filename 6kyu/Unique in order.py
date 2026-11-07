def unique_in_order(sequence):
    sequence_list = list(sequence)
    unique_list = []
    for n in sequence_list:
        if unique_list == [] or n != unique_list[-1]:
            unique_list.append(n)
    return unique_list

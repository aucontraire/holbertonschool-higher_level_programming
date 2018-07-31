#!/usr/bin/python3

def find_peak(list_of_integers):
    """Finds peak
    Args:
        list_of_integers (list): list of integers
    """
    len_lst = len(list_of_integers)
    if len_lst < 3:
        return None
    peak = list_of_integers[1]
    for i in range(1, len_lst):
        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]
    return peak

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 3, 1]))

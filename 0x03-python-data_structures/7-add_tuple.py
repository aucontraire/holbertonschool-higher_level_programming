#!/usr/bin/python3


def standardize_tuple(tup):
    tup_len = len(tup)
    if tup_len == 0:
        return (0, 0)
    elif tup_len == 1:
        return (tup[0], 0)
    else:
        return (tup[0], tup[1])


def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    tup_a_st = standardize_tuple(tuple_a)
    tup_b_st = standardize_tuple(tuple_b)
    sum1 = tup_a_st[0] + tup_b_st[0]
    sum2 = tup_a_st[1] + tup_b_st[1]

    return (sum1, sum2)

if __name__ == '__main__':
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

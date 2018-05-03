#!/usr/bin/python3


def safe_division(a, b):
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return quotient


def list_division(my_list_1, my_list_2, list_length):
    result_li = []
    for i in range(list_length):
        try:
            result_li.append(safe_division(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("out of range")
            result_li.append(0)

    return result_li


if __name__ == '__main__':
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

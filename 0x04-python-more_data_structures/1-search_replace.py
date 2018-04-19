#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = []
        for i, n in enumerate(my_list):
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
        return new_list


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)

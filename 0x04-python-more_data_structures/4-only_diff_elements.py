#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:
        return set_1 ^ set_2


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

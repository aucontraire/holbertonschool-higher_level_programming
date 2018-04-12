#!/usr/bin/python3


if __name__ == '__main__':
    import hidden_4

    name_list = dir(hidden_4)
    for st in name_list:
        if not st.startswith('__'):
            print('{:s}'.format(st))

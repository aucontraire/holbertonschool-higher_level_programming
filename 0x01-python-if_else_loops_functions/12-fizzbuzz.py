#!/usr/bin/python3


def fizzbuzz():
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz', end=' ')
        elif n % 3 == 0:
            print('Fizz', end=' ')
        elif n % 5 == 0:
            if n == 100:
                print('Buzz', end=' ')
            else:
                print('Buzz', end=' ')
        else:
            print('{:d}'.format(n), end=' ')


if __name__ == '__main__':
    fizzbuzz()

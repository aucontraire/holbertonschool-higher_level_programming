#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        sent_len = len(sentence)
        if sent_len == 0:
            return (sent_len, None)
        return (sent_len, sentence[0])


if __name__ == '__main__':
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

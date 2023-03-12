#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = None
    if x > 0:
        y = sentence[0]
    return (x, y)

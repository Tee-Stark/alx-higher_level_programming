#!/usr/bin/python3
def remove_char_at(str, n):

    if n > 0 and n < len(str) - 1:
        return str[0:n] + str[n+1:]

    elif n == len(str) - 1:
        return str[0:n-1]

    elif n == 0:
        return str[1:]

    elif n >= len(str) or n < 0:
        return str

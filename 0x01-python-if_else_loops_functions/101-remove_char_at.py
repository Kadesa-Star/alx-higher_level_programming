#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(input_str):
        return input_str
    result_str = input_str[:n] + input_str[n+1:]
    return result_str

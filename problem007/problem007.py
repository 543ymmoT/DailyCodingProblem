"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def get_decode_counts(code):
    code_int = int(code)
    
    if len(code) == 1:
        count = 1
    elif len(code) == 2:
        count = 1 + is_within_range(code_int)
    else:
        count = get_decode_counts(code[1:])
        if is_within_range(code[:2]):
            count += get_decode_counts(code[2:])
    return count

def is_within_range(code):
    code_int = int(code)
    return 1 if code_int >= 1 and code_int <= 26 else 0


assert get_decode_counts('111') == 3
assert get_decode_counts('123') == 3
assert get_decode_counts('128') == 2
assert get_decode_counts('1234') == 3
assert get_decode_counts('1111') == 5
assert get_decode_counts('12321') == 6
assert get_decode_counts('101001') == 10
assert get_decode_counts('41') == 1
assert get_decode_counts('22') == 2

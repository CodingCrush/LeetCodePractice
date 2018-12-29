def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    ret, last = 0, 0
    for c in s:
        if c == 'I':
            tmp = 1
        elif c == 'V':
            tmp = 5
        elif c == 'X':
            tmp = 10
        elif c == 'L':
            tmp = 50
        elif c == 'C':
            tmp = 100
        elif c == 'D':
            tmp = 500
        elif c == 'M':
            tmp = 1000
        if tmp > last:
            ret += (tmp - 2*last)
        else:
            ret += tmp
        last = tmp
    return ret


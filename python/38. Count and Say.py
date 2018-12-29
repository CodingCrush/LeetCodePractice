def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    ret = '1'

    for _ in range(1, n):
        tmp = ""
        head, last, count = 0, ret[0], 0
        while head < len(ret):
            if ret[head] == last:
                count += 1
            else:
                tmp = tmp + str(count) + last
                last = ret[head]
                count = 1
            head += 1
            if head == len(ret):
                tmp += (str(count) + last)
        ret = tmp
    return ret

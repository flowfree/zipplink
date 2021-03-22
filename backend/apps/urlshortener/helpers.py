import string 


class Base62(object):
    """
    Helper class for encoding/decoding with Base 62. The code is borrowed from:
    https://stackoverflow.com/a/2549514/1396314
    """

    BASE_LIST = string.digits + string.ascii_letters
    BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

    @staticmethod
    def encode(num):
        if num == 0:
            return Base62.BASE_LIST[0]
        length = len(Base62.BASE_LIST)
        s = ''
        while num != 0:
            s = Base62.BASE_LIST[num % length] + s
            num //= length
        return s

    @staticmethod
    def decode(s):
        length = len(Base62.BASE_DICT)
        ret = 0
        for i, c in enumerate(s[::-1]):
            ret += (length ** i) * Base62.BASE_DICT[c]
        return ret    

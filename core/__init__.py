def chip(func):
    def inner(*args):
        return func(*args)
    return inner

@chip
def Nand(a:bool, b:bool) -> bool:
    return not(a and b)

class InvalidInputLengthException(Exception):
    pass

def convert_to_binary16(n):
    binary = bin(n).split('b')[1]
    arr = [bool(int(x)) for x in binary]
    return [False]*(16-len(arr)) + arr

def convert_to_decimal(bits):
    t = 0
    p = 1
    for b in bits[::-1]:
        if b:
            t += p
        p *= 2
    return t


__all__ = ['gate', 'nand', 'InvalidInputLengthException']


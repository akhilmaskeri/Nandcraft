from typing import List
from core import chip, InvalidInputLengthException
from chips import Xor, And, Or

@chip
def HalfAdder(a:bool, b:bool) -> (bool, bool):
    return (Xor(a, b), And(a, b))

@chip
def FullAdder(a:bool, b:bool, c:bool) -> (bool, bool):
    hsum, hcarry = HalfAdder(a, b)
    
    _sum = Xor(hsum, c)
    _carry = Or(hcarry, And(hsum, c))

    return [_sum, _carry]


@chip
def Add16(a:List[bool], b:List[bool]) -> List[bool]:
    if len(a) != 16 or len(b) != 16:
        raise InvalidInputLengthException("required length of sel is 3")
    out = [False for _ in range(16)]

    out[0], t = FullAdder(a[0], b[0], 0)
    out[1], t = FullAdder(a[1], b[1], t)
    out[2], t = FullAdder(a[2], b[2], t)
    out[3], t = FullAdder(a[3], b[3], t)
    out[4], t = FullAdder(a[4], b[4], t)
    out[5], t = FullAdder(a[5], b[5], t)
    out[6], t = FullAdder(a[6], b[6], t)
    out[7], t = FullAdder(a[7], b[7], t)
    out[8], t = FullAdder(a[8], b[8], t)
    out[9], t = FullAdder(a[9], b[9], t)
    out[10], t = FullAdder(a[10], b[10], t)
    out[11], t = FullAdder(a[11], b[11], t)
    out[12], t = FullAdder(a[12], b[12], t)
    out[13], t = FullAdder(a[13], b[13], t)
    out[14], t = FullAdder(a[14], b[14], t)
    out[15], t = FullAdder(a[15], b[15], t)

    return out

@chip
def Inc16(_in:List[bool]) -> List[bool]:
    if len(_in) != 16:
        raise InvalidInputLengthException("required length of sel is 3")
    
    out[0], t = FullAdder(_in[0], b=t)
    out[1], t = FullAdder(_in[1], b=t)
    out[2], t = FullAdder(_in[2], b=t)
    out[3], t = FullAdder(_in[3], b=t)
    out[4], t = FullAdder(_in[4], b=t)
    out[5], t = FullAdder(_in[5], b=t)
    out[6], t = FullAdder(_in[6], b=t)
    out[7], t = FullAdder(_in[7], b=t)
    out[8], t = FullAdder(_in[8], b=t)
    out[9], t = FullAdder(_in[9], b=t)
    out[10], t = FullAdder(_in[10], b=t)
    out[11], t = FullAdder(_in[11], b=t)
    out[12], t = FullAdder(_in[12], b=t)
    out[13], t = FullAdder(_in[13], b=t)
    out[14], t = FullAdder(_in[14], b=t)
    out[15], t = FullAdder(_in[15], b=t)

    return out
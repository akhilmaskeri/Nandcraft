from typing import List
from functools import reduce
from core import chip, Nand, InvalidInputLengthException


@chip
def Not(_in: bool) -> bool:
    return Nand(_in, _in)


@chip
def Not16(_in: List[bool]) -> List[bool]:
    if len(_in) != 16:
        raise InvalidInputLengthException("required length of input is 16")
    return [Not(_in[i]) for i in range(16)]


@chip
def And(a: bool, b: bool) -> bool:
    return Not(Nand(a, b))


@chip
def And16(a: List[bool], b: List[bool]) -> List[bool]:
    if len(a) != 16 or len(b) != 16:
        raise InvalidInputLengthException("required length of input is 16")
    return [And(a[i], b[i]) for i in range(16)]


@chip
def Or(a: bool, b: bool) -> bool:
    return Nand(Not(a), Not(b))


@chip
def Or16(a: List[bool], b: List[bool]) -> List[bool]:
    if len(a) != 16 or len(b) != 16:
        raise InvalidInputLengthException("required length of input is 16")
    return [ Or(a[i], b[i]) for i in range(16) ]


@chip
def Or8Way(_in: List[bool]) -> bool:
    if len(_in) != 8:
        raise InvalidInputLengthException("required length of input is 8")
    return reduce(Or, _in)


@chip
def Xor(a: bool, b: bool) -> bool:
    return Or(And(a, Not(b)), And(Not(a), b))


@chip
def DMux(_in: bool, sel: bool) -> List[bool]:
    return [And(_in, Not(sel)), And(_in, sel)]


@chip
def DMux4Way(_in: bool, sel: List[bool]) -> List[bool]:
    if len(sel) != 2:
        raise InvalidInputLengthException("required length of sel is 2")

    not_sel_0 = Not(sel[0])
    not_sel_1 = Not(sel[1])

    return [
        And(_in, And(not_sel_1, not_sel_0)),
        And(_in, And(not_sel_1, sel[0])),
        And(_in, And(sel[1], not_sel_0)),
        And(_in, And(sel[1], sel[0])),
    ]


@chip
def DMux8Way(_in: bool, sel: List[bool]) -> List[bool]:
    if len(sel) != 3:
        raise InvalidInputLengthException("required length of sel is 3")

    sel = sel[::-1]

    p1 = And(_in, Not(sel[2]))
    p2 = And(_in, sel[2])

    return DMux4Way(p1, sel[0:2]) + DMux4Way(p2, sel[0:2])


@chip
def Mux(a: bool, b: bool, sel: bool) -> bool:
    return Or(And(a, Not(sel)), And(b, sel))


@chip
def Mux16(a: List[bool], b: List[bool], sel: bool) -> List[bool]:
    if len(a) != 16 or len(b) != 16:
        raise InvalidInputLengthException("required length of inputs is 16")
    return [Mux(a[i], b[i], sel) for i in range(16)]


@chip
def Mux4Way16(
    a: List[bool], b: List[bool], c: List[bool], d: List[bool], sel: List[bool]
) -> List[bool]:
    if len(a) != 16 or len(b) != 16 or len(c) != 16 or len(d) != 16:
        raise InvalidInputLengthException("required length of inputs is 16")
    if len(sel) != 2:
        raise InvalidInputLengthException("required length of sel is 2")

    return Mux16(Mux16(a, b, sel[1]), Mux16(c, d, sel[1]), sel[0])


@chip
def Mux8Way16(
    a: List[bool],
    b: List[bool],
    c: List[bool],
    d: List[bool],
    e: List[bool],
    f: List[bool],
    g: List[bool],
    h: List[bool],
    sel: List[bool],
) -> List[bool]:

    if (
        len(a) != 16
        or len(b) != 16
        or len(c) != 16
        or len(d) != 16
        or len(e) != 16
        or len(f) != 16
        or len(g) != 16
        or len(h) != 16
    ):
        raise InvalidInputLengthException("required length of inputs is 16")
    if len(sel) != 3:
        raise InvalidInputLengthException("required length of sel is 3")

    sel = sel[::-1]

    t1 = Mux4Way16(a, b, c, d, sel[0:2])
    t2 = Mux4Way16(e, f, g, h, sel[0:2])
    return Mux16(t1, t2, sel[2])

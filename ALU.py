from typing import List
from core import chip, InvalidInputLengthException
from chips import Mux16, Not16, And16, Or8Way, Not, Or
from Add import Add16

@chip
def ALU(x:List[bool], y:List[bool], zx:bool, nx:bool, zy:bool, ny:bool, f:bool, no:bool) -> (List[bool], bool, bool):

    xout = Mux16(x, [False]*16, zx)
    nxout = Not16(xout)
    inputx = Mux16(xout, nxout, nx)

    yout = Mux16(y, [False]*16, zy)
    nyout = Not16(yout)
    inputy = Mux16(yout, nyout, ny)

    xplusy = Add16(inputx, inputy)
    xandy = And16(inputx, inputy)

    fout = Mux16(xandy, xplusy, f)
    nfout = Not16(fout)

    out = Mux16(fout, nfout, no)
    
    nzr = Or(Or8Way(out[0:8]), Or8Way(out[8:16]))
    zr = Not(nzr)
    ng = out[15]

    return out, zr, ng

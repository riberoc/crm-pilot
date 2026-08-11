import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 533) - 594
    _mask = _data(222, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = 'T?nU9!@(S0,`O o%vA(qa>fSP%B<#W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

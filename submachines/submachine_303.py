import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 919) - 885
    _mask = _data(40, None)
    _enc = 76
    return _mask, _enc

def run():
    matrix = 'x`_MS/ i(Bf>NWI$#S%In;35#Nqv2`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 861) - 136
    _mask = _data(629, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = 'E`AEDy_8^TX[(TRRe+24Ci+^0o*_ i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

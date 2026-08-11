import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 241) - 670
    _mask = _data(917, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = '6hXung-20!OqqSDv7mDLe _oS(+5C,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

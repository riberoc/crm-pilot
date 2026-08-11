import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 354) - 773
    _mask = _data(654, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = 'iu(E4 *(0Pd@@4eM$|Rk,-5oBIrK22'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

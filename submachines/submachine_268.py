import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 591) - 831
    _mask = _data(1659, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = '=ll[p14[mRoY7Z_ndK $yDz,!xS:{+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

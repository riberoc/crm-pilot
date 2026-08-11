import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 497) - 108
    _mask = _data(167, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'lUeuN;VNcLzR`s6o 4e~y0/Zxy:kI$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

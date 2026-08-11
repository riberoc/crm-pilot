import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 654) - 659
    _mask = _data(397, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = 'nYmrXng -Zr(``FuQ*V-:yjvUYMx.J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

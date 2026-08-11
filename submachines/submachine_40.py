import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 711) - 234
    _mask = _data(957, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = 'LX/s5mYZjY~g`9iO{ 1q]hy}gF`S9*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

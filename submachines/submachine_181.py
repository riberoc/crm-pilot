import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 870) - 252
    _mask = _data(713, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = ':&<%_{z5z4x/nG} )kueY0OO4)/,Q:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

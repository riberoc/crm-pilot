import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 672) - 945
    _mask = _data(1688, None)
    _enc = 154
    return _mask, _enc

def run():
    matrix = '+UsVO&L,P:$T`zvS+?6$|$>tE}`X: '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

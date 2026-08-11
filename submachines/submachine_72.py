import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 323) - 371
    _mask = _data(245, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'mfd)x;XcLyJ0S(z]5|<_AEB9Qir}) '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

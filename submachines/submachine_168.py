import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 606) - 149
    _mask = _data(852, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = '[tzLzu01g2dZ>n;K$|n`f%O-L nVyT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

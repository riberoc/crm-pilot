import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 121) - 676
    _mask = _data(682, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'ysGzVOy)TqF8l.s<DS^GaPv<I1S eI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 183) - 637
    _mask = _data(580, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'o!:LicD-S)_$g 50H|9R!r2q}N;i?m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

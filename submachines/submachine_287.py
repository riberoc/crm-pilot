import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 567) - 856
    _mask = _data(419, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = '{4DI5S=r6H5a 3GG6xVwlztRuYNLKG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

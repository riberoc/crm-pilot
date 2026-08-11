import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 209) - 112
    _mask = _data(120, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = '/,^C7V*lST/}f%D7Ga4T HF64/+IHi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 833) - 762
    _mask = _data(122, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = 'h x6Y);t=R[eGlG`/SBCm.7x_;]x&)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 665) - 136
    _mask = _data(628, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = 'foNM^yxYLfLho?]JcU2Q^n^Aa,be {'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

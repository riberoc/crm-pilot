import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 959) - 969
    _mask = _data(1958, None)
    _enc = 82
    return _mask, _enc

def run():
    matrix = 'XU J[h.{(mF~i9XM7=qVTPQ`7.<^l.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

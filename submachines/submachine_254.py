import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 257) - 594
    _mask = _data(966, None)
    _enc = 118
    return _mask, _enc

def run():
    matrix = '`57 q!h/5pR33Ku{z/Qmihd!W9$6SL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

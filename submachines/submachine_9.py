import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 387
    _mask = _data(212, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = '6s s##&Jb74!h7iGQBcIq1`?[;in,Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

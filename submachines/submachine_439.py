import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 672) - 379
    _mask = _data(795, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = 'rqE<egf]1!R)U_J8, bl1)dquA9e.c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

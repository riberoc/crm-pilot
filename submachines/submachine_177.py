import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 391) - 888
    _mask = _data(610, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = 'X$(TyAAt g`{tYZMj6GZb.]HtMx%4m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

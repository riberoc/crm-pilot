import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 105) - 476
    _mask = _data(765, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = '%0uRj`nezCnwNijH@o%Q].//t $$C`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 339) - 291
    _mask = _data(31, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'mw5PrD:um3-37u.!n9gDJez/_+S7b '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

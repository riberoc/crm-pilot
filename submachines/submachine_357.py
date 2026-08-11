import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 496) - 342
    _mask = _data(970, None)
    _enc = 252
    return _mask, _enc

def run():
    matrix = 'l%ohjjoQ(9LB?kXs4x0.~#eC 2bz8Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

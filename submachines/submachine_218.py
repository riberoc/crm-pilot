import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 645) - 631
    _mask = _data(60, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = '#h*+/In5`:9hJ`su<T%@~#4:gn=3fs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

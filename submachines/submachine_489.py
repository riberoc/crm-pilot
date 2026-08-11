import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 783) - 939
    _mask = _data(1920, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = ')X0geyC2d9wHhrMvjh?(<[`Ft1oLdy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

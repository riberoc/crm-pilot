import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 270) - 421
    _mask = _data(228, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'H1&>S^I<LD~6B7hJ0gZE`Qj9jiOtKF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

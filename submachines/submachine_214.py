import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 504) - 409
    _mask = _data(18, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = '1+6KqoS+Lm<# e8d@h!*j#L%B$Y-7b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

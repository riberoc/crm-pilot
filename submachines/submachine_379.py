import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 975) - 500
    _mask = _data(391, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = '%cfYrW},MUH>|rDoOV&w O-;H(pd52'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

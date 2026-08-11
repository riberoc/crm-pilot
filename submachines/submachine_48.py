import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 636) - 855
    _mask = _data(435, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = '^NJv{-B2ZtP bF3^QJ|{))sii>e:#S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

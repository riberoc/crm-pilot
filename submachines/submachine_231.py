import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 839) - 991
    _mask = _data(1898, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = '&F/PrA`lF#zHG%+-Wc<In@K= Kh0}%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

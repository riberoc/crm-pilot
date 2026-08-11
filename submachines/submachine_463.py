import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 326) - 389
    _mask = _data(871, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = 'u<BJ@=V4*q1R/(M`.(~hk 18q~7{5m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

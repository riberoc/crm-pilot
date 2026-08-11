import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 708) - 624
    _mask = _data(418, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = 'v,7I-K~uN/5@+xw|Vpuo~+7io/~a;F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

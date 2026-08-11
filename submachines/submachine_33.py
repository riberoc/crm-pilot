import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 124) - 227
    _mask = _data(413, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'fGs&W]PzXVL`tKD<bqM2e7i!yo2+.]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

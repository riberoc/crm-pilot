import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 900) - 645
    _mask = _data(218, None)
    _enc = 195
    return _mask, _enc

def run():
    matrix = '(OZ7R9b|i|L$X}EPoSpw).LbKyrS/6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

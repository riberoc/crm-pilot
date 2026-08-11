import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 284) - 773
    _mask = _data(565, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = 'uw3 RM{_rrFftyB{eC.b;:S::@K5?a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

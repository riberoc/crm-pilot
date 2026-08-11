import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 934) - 205
    _mask = _data(853, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = '61. m(Z[e7sB~90&ANl}It^~jTP(|j'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

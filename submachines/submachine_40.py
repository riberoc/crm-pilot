import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 913) - 429
    _mask = _data(311, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = '|S+)N$7z5( Qq3{5q<8@.mJzoqf^1t'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

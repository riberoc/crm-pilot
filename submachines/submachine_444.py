import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 439) - 506
    _mask = _data(866, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = '6bWuLx(a~W[:{@,pdzkfmp35({.v%o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

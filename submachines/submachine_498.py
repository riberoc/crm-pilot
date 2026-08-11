import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 428) - 745
    _mask = _data(668, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = 'sYhU {!YJ]}{]WK}c.l#CIxCK%R2}c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

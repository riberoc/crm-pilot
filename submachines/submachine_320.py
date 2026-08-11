import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 154) - 261
    _mask = _data(497, None)
    _enc = 114
    return _mask, _enc

def run():
    matrix = 'jfR%:@{#.9=v?ij,7/`s 2^<bv!>u/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

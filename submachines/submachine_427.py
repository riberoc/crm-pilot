import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 430) - 589
    _mask = _data(651, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'Ink*?;(xCT5 UHah.C!j{q[_c-?`p:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

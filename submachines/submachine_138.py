import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 671) - 719
    _mask = _data(125, None)
    _enc = 29
    return _mask, _enc

def run():
    matrix = '=5nOh1fX.~(w`h 3V7kymnkg]f_`K^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

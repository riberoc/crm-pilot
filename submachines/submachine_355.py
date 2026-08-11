import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 483) - 819
    _mask = _data(609, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = ' pm])]QS)v>7L5dk?5Dp!#*22Q!Yft'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 130) - 903
    _mask = _data(892, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = ';GE87{TzJbf^g(pcc6fdf|4};DL EF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

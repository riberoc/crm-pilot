import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 700) - 374
    _mask = _data(870, None)
    _enc = 124
    return _mask, _enc

def run():
    matrix = '^(CE(!EY3?Mr*AkVZ>;X$U/d |//A+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 749) - 634
    _mask = _data(123, None)
    _enc = 15
    return _mask, _enc

def run():
    matrix = '~_JUnyy0<rVfVL1FR77 ^>?o(b+m/)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

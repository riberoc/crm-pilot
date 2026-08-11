import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 279
    _mask = _data(392, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = '97R(+vyQ x&J[$JI6F0,3!Z`zi`Yoa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

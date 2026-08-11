import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 442) - 526
    _mask = _data(991, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = 'tG]vH47vpvmpzIm+*jt2o6Si3 ~Cw/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

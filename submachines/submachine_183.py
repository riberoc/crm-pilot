import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 688) - 343
    _mask = _data(225, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = '#As/J[.5,^QX $|*B28!p+Bx;iu(%a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

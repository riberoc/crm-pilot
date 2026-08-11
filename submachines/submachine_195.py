import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 122) - 470
    _mask = _data(683, None)
    _enc = 227
    return _mask, _enc

def run():
    matrix = '`1t#2,K)%5,^Rpr~LI<2`~Xo CfxLk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

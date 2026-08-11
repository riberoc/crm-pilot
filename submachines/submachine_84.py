import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 280) - 787
    _mask = _data(634, None)
    _enc = 82
    return _mask, _enc

def run():
    matrix = 'wKUb2Mvh-gB0[5i`b+Sd7=.|E>XyF '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

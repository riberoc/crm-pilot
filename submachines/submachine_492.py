import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 628) - 131
    _mask = _data(735, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = '^>9ez>HY<Ho1X2] %sd*kKW{@8u,R|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

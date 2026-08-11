import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 669) - 497
    _mask = _data(144, None)
    _enc = 11
    return _mask, _enc

def run():
    matrix = 'T+FSm;>s<rptH:#S?DJe|lR <kUR:e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

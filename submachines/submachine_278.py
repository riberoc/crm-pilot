import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 776) - 828
    _mask = _data(161, None)
    _enc = 102
    return _mask, _enc

def run():
    matrix = '&QJNl(gps~_ DGz?8KH,%9`uq]*W7M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

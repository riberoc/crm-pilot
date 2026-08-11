import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 420) - 824
    _mask = _data(1444, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = 'd|7<ZRmhg$a*>F$nK L=#nlag^j:QV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

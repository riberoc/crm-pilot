import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 292) - 709
    _mask = _data(650, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = '+bn`p+d!<aoc=Dq`z$_ b4BSQXD(xm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

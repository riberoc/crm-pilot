import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 397) - 873
    _mask = _data(580, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = 'qLrMz9[jgl^ey duM5Hs?6*LHOUygr'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 945) - 702
    _mask = _data(143, None)
    _enc = 155
    return _mask, _enc

def run():
    matrix = 'ZOG*^J9tq=O*87Fy*Gf*)d.4>*X |W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

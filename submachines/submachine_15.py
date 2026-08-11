import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 334) - 672
    _mask = _data(545, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = '0+rVN@~}CIP#+3nC}=%5 :;9Do4#w:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

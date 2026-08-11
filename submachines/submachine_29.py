import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 556) - 917
    _mask = _data(1542, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = '(k?<=_(1L9 XGG:;geKqg;/3IT@|SX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 681) - 958
    _mask = _data(1666, None)
    _enc = 97
    return _mask, _enc

def run():
    matrix = 'PK4kmz)t.Sjl 7TzGkOem7Q2?0oUp`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

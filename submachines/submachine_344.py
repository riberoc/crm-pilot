import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 114) - 810
    _mask = _data(788, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'A|D;Kh6HU@]/}NKo>nWPIKcutTB]t!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 624) - 606
    _mask = _data(197, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'S c=%xA~/X.Z9YGt{_QWnpRY<P3lp<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 721) - 375
    _mask = _data(771, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = '*+?-E0lpcziTZBmXuUXTq{ (G7=/Xi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

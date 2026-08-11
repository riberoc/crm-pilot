import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 560) - 316
    _mask = _data(60, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = 'cFZD4d6YZb!B)k]b @*8`5P5]*_7P$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

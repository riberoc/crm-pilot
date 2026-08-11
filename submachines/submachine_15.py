import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 608) - 326
    _mask = _data(996, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = '(za|ndQ_tka)I0)yK5-lte|6gL5FFt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

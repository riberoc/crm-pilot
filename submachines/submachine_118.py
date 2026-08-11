import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 420) - 852
    _mask = _data(732, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = '?3pw)8vwqkF[y6[3I+hm~MKmOjd4D+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 113) - 616
    _mask = _data(643, None)
    _enc = 152
    return _mask, _enc

def run():
    matrix = '[06y_K?AA`#c;4!A4Q QHM:W[XXang'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

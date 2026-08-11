import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 331) - 379
    _mask = _data(786, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = '>r?8axl?93D(cTyA@bCWnnzq3 #`~#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

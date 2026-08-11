import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 710) - 319
    _mask = _data(914, None)
    _enc = 27
    return _mask, _enc

def run():
    matrix = 'Y6Kkv7>7Hpm|FXhr|i0CuC08uSKJC#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

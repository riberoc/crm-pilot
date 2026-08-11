import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 110) - 567
    _mask = _data(885, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '>s}E+NJ`Ka~^o6nmn6xK}f($MhhUWj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 980) - 907
    _mask = _data(14, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = 'B&_TrZ}|xfo|`g9j^i]m&%BeaE y{A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

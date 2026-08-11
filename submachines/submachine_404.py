import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 753) - 297
    _mask = _data(864, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = '1$Z)^j.g,M//UiDZ &?R:p[gtn(%iO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

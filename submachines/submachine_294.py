import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 301) - 253
    _mask = _data(158, None)
    _enc = 172
    return _mask, _enc

def run():
    matrix = '-Z/]uX<rLEVJ%&^#3,E0cEH#eL D*/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

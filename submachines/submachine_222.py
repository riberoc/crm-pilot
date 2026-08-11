import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 102) - 763
    _mask = _data(781, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = '.2j3[^Ij6s^Yb`Tablz d_2R3lMziO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

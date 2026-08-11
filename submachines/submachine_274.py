import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 585) - 603
    _mask = _data(128, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'A)G_~B0[5k<f$RKBo?B^Y 1nw^,4dK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

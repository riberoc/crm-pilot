import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 780) - 451
    _mask = _data(352, None)
    _enc = 169
    return _mask, _enc

def run():
    matrix = ' P}6-wnkrwAnSUXt*CxPR2;mnyZpX='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

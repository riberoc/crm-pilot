import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 827) - 846
    _mask = _data(1820, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'y$B[vd!>u H~6NA9vndmYX$VUA%;gc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

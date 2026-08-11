import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 287) - 235
    _mask = _data(218, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = 'wHP*^Z TJ;@)-dUWn`{@;o33ViA%YC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

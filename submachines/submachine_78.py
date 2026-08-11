import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 309) - 680
    _mask = _data(964, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'iHEjaZx8TKLIUC6z->vA??Wk@%r%M0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

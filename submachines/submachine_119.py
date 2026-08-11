import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 125) - 965
    _mask = _data(899, None)
    _enc = 59
    return _mask, _enc

def run():
    matrix = 'ys p_:MUGcet1O,%}@O]>.X$qp0KWA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

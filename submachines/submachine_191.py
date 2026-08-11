import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 355) - 415
    _mask = _data(1011, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'jn?j08E|6!Y3Q(iWR Y!B_s&i86},,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

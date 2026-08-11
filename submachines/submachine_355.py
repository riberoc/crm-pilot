import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 679) - 311
    _mask = _data(774, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = '*(! Wx~js_t0IMZ_~H>dk4jIxdPtas'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

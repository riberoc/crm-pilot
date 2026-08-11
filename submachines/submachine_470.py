import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 213) - 500
    _mask = _data(593, None)
    _enc = 141
    return _mask, _enc

def run():
    matrix = 'vuLKq!yp&[J:<eDv$DZ9zes?kv/`g '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

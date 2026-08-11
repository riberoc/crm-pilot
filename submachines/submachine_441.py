import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 417) - 878
    _mask = _data(569, None)
    _enc = 32
    return _mask, _enc

def run():
    matrix = '!RAmwn$e<w {LvqwVDJ&1`$+j~#HS7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

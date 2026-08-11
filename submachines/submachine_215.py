import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 395) - 773
    _mask = _data(628, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = '`{)N91o](p!:im{y)taavWpquNgoJ7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

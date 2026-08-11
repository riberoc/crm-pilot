import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 456) - 673
    _mask = _data(787, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'a!@o*7;LE7|OH;aK`?Hd.h?Sy0iX>8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

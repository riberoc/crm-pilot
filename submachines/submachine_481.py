import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 701) - 893
    _mask = _data(1707, None)
    _enc = 156
    return _mask, _enc

def run():
    matrix = 'uc7#y Cy9QWp~Yd4QN4#Pi`5J0@cAo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

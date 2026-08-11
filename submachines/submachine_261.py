import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 525) - 856
    _mask = _data(460, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'ZT?sAD9V4JUyiaC.|YF0v/eNzFro4]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

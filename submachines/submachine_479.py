import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 699) - 760
    _mask = _data(473, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = 'c+q J4aAX@lIEUd{Bu8=f4KMXVu0zc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 381) - 499
    _mask = _data(913, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = '-9t(Bu ]wC35SR97oVH:*h;/`E`sI.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

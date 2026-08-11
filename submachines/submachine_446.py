import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 627) - 368
    _mask = _data(912, None)
    _enc = 113
    return _mask, _enc

def run():
    matrix = 'E. @f}W9i^b4+{rk)1+b3$5a[3U@0@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

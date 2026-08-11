import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 374) - 654
    _mask = _data(933, None)
    _enc = 71
    return _mask, _enc

def run():
    matrix = '#q oxaUy~]IBZr<7EAu}>[kf@q0VyW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

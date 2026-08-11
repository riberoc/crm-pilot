import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 448) - 744
    _mask = _data(678, None)
    _enc = 122
    return _mask, _enc

def run():
    matrix = '/Zml a*/@S8Bn|;],tN3I7=LQQa$Et'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

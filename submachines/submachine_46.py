import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 973) - 829
    _mask = _data(2036, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = '+:?>:Z!lj[M:zYeA0|B4x&e6=o340y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

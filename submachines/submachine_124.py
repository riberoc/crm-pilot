import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 406) - 672
    _mask = _data(682, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = '?4lIz[j6C_,=u&%SPKXg:y#wT20C5 '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

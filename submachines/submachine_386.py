import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 505) - 555
    _mask = _data(942, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = '<HK-7xo%s?O)nl)YIsSwF[iw{rLm@9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

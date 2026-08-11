import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 280) - 313
    _mask = _data(798, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = 'z^g*z&m6gzFYCub1T[lqm *<P47<Wb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

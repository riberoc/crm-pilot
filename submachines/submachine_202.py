import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 795) - 470
    _mask = _data(307, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = '3JxhyM*Q6$YG &vgo<b;J$55&jI2kp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

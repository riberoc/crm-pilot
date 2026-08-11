import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 892) - 299
    _mask = _data(565, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = '#ILk^) $9_eLeH-VrxcqnQPFlG3H=W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

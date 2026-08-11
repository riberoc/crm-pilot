import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 517) - 199
    _mask = _data(783, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'k7tCwa?y12T4Ar1+KQhoDg< ZeR*a_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

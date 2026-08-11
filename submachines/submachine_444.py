import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 460) - 549
    _mask = _data(778, None)
    _enc = 183
    return _mask, _enc

def run():
    matrix = 'PTjmAet-/B}._t)>}g?W~u <u1[^=s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 843) - 558
    _mask = _data(446, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = 'RuxZVh{4fYuoS`j?L#TmeOJ12@?1 A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

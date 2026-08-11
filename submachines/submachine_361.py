import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 505) - 496
    _mask = _data(889, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'H5dq O4_C%O0k42VySR<o1KwWyXxDi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

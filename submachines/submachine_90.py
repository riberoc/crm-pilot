import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 204) - 490
    _mask = _data(640, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = 'EF 7lj1bDaDk)3*niaWjtr(e3(C8nQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

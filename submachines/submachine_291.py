import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 343) - 954
    _mask = _data(1483, None)
    _enc = 248
    return _mask, _enc

def run():
    matrix = '8NcvK0@%lT1b#[;1./a}@[cR@= |]~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

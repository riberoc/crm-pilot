import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 753
    _mask = _data(422, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = 'udU$J3VO{ag/eE`.c4[$]6 Sk0J55X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

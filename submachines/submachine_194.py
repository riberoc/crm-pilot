import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 975) - 175
    _mask = _data(721, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'W+YowBt|@%&<$?M4|yPg _TJ[6SqMu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

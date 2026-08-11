import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 311) - 399
    _mask = _data(211, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'Agmj^Fo9RQ_ `4*PG6zo4)7H9(}c$+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

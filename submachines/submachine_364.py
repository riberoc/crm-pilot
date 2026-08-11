import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 370) - 980
    _mask = _data(1477, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = '<eVNUY-z3<`pj9O EV`&|ys,(ebcEj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

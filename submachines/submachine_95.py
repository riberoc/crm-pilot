import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 844) - 561
    _mask = _data(433, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = ':NL}h;e:z3 qAu#RhZ&^Yf}xJYdK*;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

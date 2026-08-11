import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 664) - 511
    _mask = _data(164, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = ') NqTncp:~JT-&Z`8ECsYNw+ib*uw@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

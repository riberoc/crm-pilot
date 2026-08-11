import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 492) - 712
    _mask = _data(591, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 'f(ETW3$pPI#bw.{?ze !XV+<a47U3='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

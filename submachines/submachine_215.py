import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 536
    _mask = _data(941, None)
    _enc = 0
    return _mask, _enc

def run():
    matrix = '8B,_-6(B_[%U3!o#:mz2 -J@whv%]&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

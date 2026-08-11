import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 979) - 979
    _mask = _data(2010, None)
    _enc = 32
    return _mask, _enc

def run():
    matrix = ';BDSLq5h7i(Z]BWkOb0|@k @Xi:b-m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 968) - 586
    _mask = _data(280, None)
    _enc = 154
    return _mask, _enc

def run():
    matrix = 'F8gqF5hS*K1<:/4+0I*;8>4E/rt| #'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

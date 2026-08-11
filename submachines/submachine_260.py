import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 902) - 530
    _mask = _data(427, None)
    _enc = 19
    return _mask, _enc

def run():
    matrix = 'R`NxJ+.e A<|t;|6lIZvStId&3NE?e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

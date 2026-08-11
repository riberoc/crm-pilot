import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 167) - 672
    _mask = _data(920, None)
    _enc = 152
    return _mask, _enc

def run():
    matrix = '#)s@>5q A6dJe|;U1!orxE{Ve>+Z`A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

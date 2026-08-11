import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 402) - 456
    _mask = _data(797, None)
    _enc = 194
    return _mask, _enc

def run():
    matrix = ':g+KyIA+=:>]+.n/=lP;:!X3$q+v(]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

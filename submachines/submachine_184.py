import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 680) - 534
    _mask = _data(43, None)
    _enc = 102
    return _mask, _enc

def run():
    matrix = '-T]ve/+g6dS 8*:;lC~vPn%ln#?ico'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

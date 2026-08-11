import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 506
    _mask = _data(492, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = '-#T2WSwU?iG>T?df+p+%zjkfy(7Sgy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

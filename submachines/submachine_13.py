import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 965) - 207
    _mask = _data(622, None)
    _enc = 209
    return _mask, _enc

def run():
    matrix = '@g?H7]b9MQU.3 b#z{uo&}CBuS?P.3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

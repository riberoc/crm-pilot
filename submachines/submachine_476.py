import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 672) - 947
    _mask = _data(1592, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = 'd6e>)?` piWH]B_W9CD<SlPf[}Q}q&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

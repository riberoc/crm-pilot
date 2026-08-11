import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 660
    _mask = _data(997, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = '#<5=dbEbPO@?0I5P9l;drSXx%Ho. p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

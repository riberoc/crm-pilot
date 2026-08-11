import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 811) - 251
    _mask = _data(538, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = 'GA`AT; ZZ>GAFLKh4`o[SSX;Q|4e;['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 801) - 968
    _mask = _data(196, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = 'x#r)6 l=GvG$<jgAp9RUx17C,S]Y};'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

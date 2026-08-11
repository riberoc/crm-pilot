import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 759) - 214
    _mask = _data(855, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = '23dpQ/<Li&w3m{c@(n ?PX]4}TwI1O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

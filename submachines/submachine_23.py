import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 942) - 357
    _mask = _data(489, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = 'v~N`GmrBj@6}T9>9Dx jn_0/Oe0s,M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

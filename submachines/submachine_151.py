import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 206) - 519
    _mask = _data(520, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'HaY^jyroVc9#OfHE<=KA0<fsh~ <Rr'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

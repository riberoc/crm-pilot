import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 609) - 314
    _mask = _data(124, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'QS:d ^CTiAp+A#pu$6[#:(tI1;L)+t'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

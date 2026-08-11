import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 811) - 745
    _mask = _data(12, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'vX^X-0(~nS&vw)4lipdtG807rB<{cZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

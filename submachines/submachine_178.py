import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 287) - 967
    _mask = _data(709, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = '}*vt)^7M.Qn u-!D_B{[Es8>q5yu:X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

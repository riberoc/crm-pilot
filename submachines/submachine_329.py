import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 501) - 801
    _mask = _data(604, None)
    _enc = 157
    return _mask, _enc

def run():
    matrix = 'j)X.U=0Os!y2i+0:V247;aPkf?&C-B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

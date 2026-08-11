import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 322) - 246
    _mask = _data(255, None)
    _enc = 196
    return _mask, _enc

def run():
    matrix = 'K2o _.R5^o=u43FI.Nv$LO+/9cNE$J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

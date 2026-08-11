import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 643) - 195
    _mask = _data(778, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = '*N%#y|_`~+Qk:.&2*CP<G4*> m;qTm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

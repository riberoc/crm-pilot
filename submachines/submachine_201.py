import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 261) - 113
    _mask = _data(81, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'Xf]G[^^|GH}VTeuKP(XApn8G/F;|%k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

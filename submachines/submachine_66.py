import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 869) - 526
    _mask = _data(488, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = '<X,23i0 4;$P*NM;qG!`6-FD81.f[7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

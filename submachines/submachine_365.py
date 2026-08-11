import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 708) - 424
    _mask = _data(827, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = '27 .?fW@(fm5_M2TrLi>iv(M(vs,>&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

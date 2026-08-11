import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 547) - 691
    _mask = _data(295, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = '#ZlndZqynv0-cVTrUr-}b_H_*^9V{4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

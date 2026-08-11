import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 648) - 374
    _mask = _data(887, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = 'D$mMzt# Y*I-%bryAxy!43k}qT4YX@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

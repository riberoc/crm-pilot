import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 210) - 491
    _mask = _data(702, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = ':xiWNp.6fBx{l|lbcqYsrF~IJD5Fb$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

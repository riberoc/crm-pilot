import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 501) - 260
    _mask = _data(149, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = 'pY/o<pccJhE=<5H|/NE v+;czXU?yt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

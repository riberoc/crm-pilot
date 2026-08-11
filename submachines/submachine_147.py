import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 805
    _mask = _data(544, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = '-`=-2-?sOQMOW-K|=P:KhljRZfm (L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

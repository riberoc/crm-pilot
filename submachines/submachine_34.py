import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 754) - 341
    _mask = _data(245, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = '42Z }4n1`f1<>EYpOax@K3oXG20u&i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 754) - 416
    _mask = _data(223, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'sd(X/k7#[r0yYz Dl?yri}AE;*N,o$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 442) - 212
    _mask = _data(139, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = '%h}<_V6=9:T!1+e-m0H%6 <I*}e5Aa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

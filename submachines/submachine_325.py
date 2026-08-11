import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 816) - 668
    _mask = _data(83, None)
    _enc = 206
    return _mask, _enc

def run():
    matrix = 'SC{dg}yhM sd^:7C:C>1g0;|5jvha|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

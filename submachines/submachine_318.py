import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 410) - 485
    _mask = _data(816, None)
    _enc = 193
    return _mask, _enc

def run():
    matrix = '1.b[ vzz>6LQ,`Ymt5j)3?@hz[M$*b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

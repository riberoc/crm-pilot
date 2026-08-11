import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 188
    _mask = _data(894, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = ')CCuTuSAkF9Rld50@Q 8(~JdXo,q,]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

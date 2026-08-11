import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 891) - 866
    _mask = _data(1882, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'tX sH9|AW^vU1}A/{>fIk#D.hCf#92'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

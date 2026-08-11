import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 356) - 286
    _mask = _data(196, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = 'yV9Q?k,L61.Eh#HfBA]UK+6%ee:(tx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

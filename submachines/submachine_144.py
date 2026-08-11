import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 491) - 958
    _mask = _data(1459, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = '[36ZD_as)>JR,&J= W_t^$)UghZVe^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

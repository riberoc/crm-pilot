import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 595) - 521
    _mask = _data(55, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = 'q3y_[t lq0x*W,#:6-^})CxU2>k$UY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

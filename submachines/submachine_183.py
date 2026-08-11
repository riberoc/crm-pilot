import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 261) - 636
    _mask = _data(578, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = '<(HE{hJY?FP)U>QkOM Z3q6s%BoyQQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

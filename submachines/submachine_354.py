import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 748) - 785
    _mask = _data(346, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = '0/cFvoL3kE,R%B>J=U=0`:h}d^? Wp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

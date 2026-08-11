import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 566) - 113
    _mask = _data(695, None)
    _enc = 4
    return _mask, _enc

def run():
    matrix = '>LSS%_g-#X1$%`;RcQVv ,0Bh<|Dhs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

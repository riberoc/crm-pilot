import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 420) - 961
    _mask = _data(1520, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = ')*A/A#(q0(}j=_lk2j3PC<$0&@ G6L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

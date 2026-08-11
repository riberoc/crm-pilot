import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 730) - 756
    _mask = _data(348, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = ' XpAS=lvWPU3zMefM{l:?R#L>}64!#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

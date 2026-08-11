import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 338) - 815
    _mask = _data(521, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 'H,xa2 uxe{PEMdI{UfhC>28{7}fYqS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 393) - 614
    _mask = _data(703, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'z!lFKL8tedK0PO>v}Fscy%S/0e- >6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

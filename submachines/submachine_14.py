import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 494) - 350
    _mask = _data(58, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'A1bg,<Io0kl81DF#%NQhIa$1L+6Bbl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

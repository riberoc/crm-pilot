import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 447) - 301
    _mask = _data(21, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = 'CP6piQ)<)zP36$etP@k5jiRX nT0vV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

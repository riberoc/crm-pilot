import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 133) - 767
    _mask = _data(847, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = '*FyRSsij6DiV]z%KttoX3 Cu{z.|1k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

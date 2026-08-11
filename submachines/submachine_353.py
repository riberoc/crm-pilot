import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 330) - 436
    _mask = _data(778, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = 'QHTsk/d|SltKU =t!OptCA27Ol~KE`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

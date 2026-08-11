import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 432
    _mask = _data(296, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = 'lh?O: :ge<ZQDv?i-b#BzTCTTQR$!u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

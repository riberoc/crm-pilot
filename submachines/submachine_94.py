import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 880
    _mask = _data(1920, None)
    _enc = 174
    return _mask, _enc

def run():
    matrix = 'pJyGZO3sf(mKj 4!x1#8d~ZD/CJg/?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 660) - 297
    _mask = _data(157, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'eJ~kFHdbo#x0iMqRVL1|#-9I%x`FfR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

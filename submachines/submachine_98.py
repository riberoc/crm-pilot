import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 250) - 395
    _mask = _data(356, None)
    _enc = 11
    return _mask, _enc

def run():
    matrix = 'UOp6P*08x+e!&?tCc2MT8:9: MFoq+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

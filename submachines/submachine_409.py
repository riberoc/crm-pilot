import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 442
    _mask = _data(636, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = '>]{D:e90ILT-49(Z_Zq6]I-gkt9C%<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

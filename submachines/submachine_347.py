import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 173) - 141
    _mask = _data(73, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = '.T3x!HY<S`1vudF.Cmyj>PhfbYm:yD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

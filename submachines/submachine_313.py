import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 634) - 833
    _mask = _data(481, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'FV!;t`0s[3OS2]U+u+ymZM@{(IQ YH'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 537) - 991
    _mask = _data(1604, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = ' Xg`5pwuu`9]N9/t:8wj=^@Tqn<w4Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

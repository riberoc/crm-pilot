import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 137) - 126
    _mask = _data(456, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'r;PE {NcZrN1gwZ#?[%^)HKdbF5$k&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 991) - 515
    _mask = _data(388, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = 'x6mF3^^WDm$P$^f]c{$8Ku%(RjO1xx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

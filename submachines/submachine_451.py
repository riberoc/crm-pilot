import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 424) - 860
    _mask = _data(1465, None)
    _enc = 173
    return _mask, _enc

def run():
    matrix = '5b/p7P1EC)A;.?KeX/^q4Bc+ JZhc$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 925) - 974
    _mask = _data(1844, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = 'wgzNp4Xsk:E5[)]9i 78A$ox7<9~1x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 178) - 538
    _mask = _data(588, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = '7~@|1XwPg7CHS7P=s8 t64L,.O_XT}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

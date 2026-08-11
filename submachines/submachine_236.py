import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 690) - 488
    _mask = _data(195, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = '@+v B0xE@$-Af9fDx3ssXh|A*mY$DY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

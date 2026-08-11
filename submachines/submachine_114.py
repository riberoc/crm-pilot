import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 507) - 518
    _mask = _data(790, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = 'R#{lAkgrGHX%*vb3, g$CZ(x5QqSHo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

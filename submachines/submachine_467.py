import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 682) - 218
    _mask = _data(802, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'Kw3?_xMGF?kmko[WhNRK*A7rab :GM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

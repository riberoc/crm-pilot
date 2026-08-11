import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 502) - 295
    _mask = _data(998, None)
    _enc = 252
    return _mask, _enc

def run():
    matrix = 'WN[)%$hySG8%^[0FUNa8% s?fz(_Tm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 142) - 458
    _mask = _data(719, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = ' $@7J0O7)LHUlGFZA~Z]J8g/dT(L+}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

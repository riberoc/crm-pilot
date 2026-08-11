import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 439) - 704
    _mask = _data(724, None)
    _enc = 173
    return _mask, _enc

def run():
    matrix = 'ch?rY3}Mw<j|]RUG9)m(=S&.pypuB2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

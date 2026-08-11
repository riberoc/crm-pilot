import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 439) - 368
    _mask = _data(950, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = '{d8X&Iw4d:87I9Hw[1mi? ~=rL=beN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

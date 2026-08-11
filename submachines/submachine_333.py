import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 745) - 662
    _mask = _data(486, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = ':& $)GO?-1P3.S#5l,AoXQvzJ4TyYp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

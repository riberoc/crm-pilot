import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 827) - 828
    _mask = _data(88, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = 'Cbn,;~&_na?[zI~g{AvVM1_a%}uJ).'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

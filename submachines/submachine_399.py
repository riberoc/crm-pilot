import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 293
    _mask = _data(622, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'ejtD0A+_a03 ?koz.0(:f&oDD;bi79'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

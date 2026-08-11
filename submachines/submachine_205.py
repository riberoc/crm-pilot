import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 112) - 285
    _mask = _data(422, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = 'qsom.i2 -3BIA`KClCH(j/K.D($MZ}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

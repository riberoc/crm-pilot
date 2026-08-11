import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 450) - 511
    _mask = _data(811, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = 'tOUtknfz8B9a(1YO::[Qudril|e #d'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()

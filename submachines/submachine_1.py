import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 821) - 655
    _mask = _data(385, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = ' wB|nOsyUlPh=%1$@&ojN&QElP0.5w'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
